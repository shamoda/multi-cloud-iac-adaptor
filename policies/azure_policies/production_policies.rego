package production

import data.terraform.plan_functions
import data.terraform.tag_validation
import input.resource_changes

# Required tags for all resources
required_tags := {"environment","technical_owner"}
validTagValues = {"prod", "nonprod"}
environment_key = "environment"
max_deletions := 0
whitelist_cidr_blocks := ["10.0.0.0/24", "192.0.0.0/24"]
prod_allowed_ports := ["22","443"]

# =================================== Warn about all deletes ===================================
resources_removed := plan_functions.get_resources_by_action("delete", resource_changes)

warn[msg] {
    count(resources_removed) > max_deletions
    msg := sprintf("By applying, you are about to destroy %d resources from the existing stack.", [count(resources_removed)])
}



# =================================== Check to see if there are Virtual networks missing tags ===================================
vnets := plan_functions.get_resources_by_type("azurerm_network_security_group", resource_changes)

tags_contain_required(resource_checks) = resources {
    resources := [ resource | 
      resource := resource_checks[_]
      not (tag_validation.missingTags(resource, required_tags))
    ]
}

deny[msg] {
    resources := tags_contain_required(vnets)
    resources != []
    msg := sprintf("The following mandatory tags are missing: %v", [required_tags])
}



# =================================== checking tag values ===================================
checkRequiredTagValueExists(tag_key) {
    # resource_changes[resource_index].change.actions[_] == "create"
    tag_value := resource_changes[resource_index].change.after.tags[tag_key]
    validTagValues[_] == tag_value
}

deny[msg] {
    resources := tags_contain_required(vnets)
    resources == []
    not checkRequiredTagValueExists(environment_key)
    msg := sprintf("Required tag value is missing for tag key: environment. Valid values are %v.", [validTagValues])
}


# =================================== in prod only 443 should be allowed ===================================
checkRequiredTagAndValueExists(tag_key,tag_value) {
    # resource_changes[resource_index].change.actions[_] == "create"
    value := resource_changes[resource_index].change.after.tags[tag_key]
    value == tag_value
}

sg_rules := plan_functions.get_resources_by_type("azurerm_network_security_rule", resource_changes)

checkPortAllowed(resource_checks, port) = port_violations{
    port_violations := [ resource | 
      resource := resource_checks[_]
      resource.change.after.destination_port_range != port[0]
      resource.change.after.destination_port_range != port[1]
    ]
}

deny[msg] {
    checkRequiredTagAndValueExists(environment_key,"prod")
    resources := checkPortAllowed(sg_rules, prod_allowed_ports)
    resources != []
    msg := sprintf("Destination port must be one of the following in prod environments: %v",[prod_allowed_ports])
}


# =================================== block port 22 ===================================
checkPortDenied(resource_checks, port) = port_violations{
    port_violations := [ resource | 
      resource := resource_checks[_]
      resource.change.after.destination_port_range == port
    ]
}

deny[msg] {
    resources := checkPortDenied(sg_rules, "22")

    port_whitelisted := [ resource | 
      resource := resources[_]
      whitelist_cidr_blocks[_] == resource.change.after.source_address_prefix
    ]

    resources != []
    port_whitelisted == []

    msg := sprintf("SSH port 22 is is only allowed for whitelisted IPs %v",[whitelist_cidr_blocks])
}