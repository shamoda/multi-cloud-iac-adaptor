from flask import request
from constructs import Construct
from imports import network_security_rule

class Azure_Network_Security_Rule_Processor():
    def __init__(self):
        pass

    def get_azure_network_security_rule(self, scope: Construct, module_json: request):
        tfId = module_json.get('tfId')
        name = module_json.get('name')
        priority = module_json.get('priority')
        direction = module_json.get('direction')
        access = module_json.get('access')
        protocol = module_json.get('protocol')
        source_port_range = module_json.get('sourcePortRange')
        destination_port_range = module_json.get('destinationPortRange')
        source_address_prefix = module_json.get('sourceAddressPrefix')
        destination_address_prefix = module_json.get('destinationAddressPrefix')
        resource_group_name = module_json.get('resourceGroupName')
        network_security_group_name = module_json.get('networkSecurityGroupName')
        return network_security_rule.NetworkSecurityRule(scope, tfId, name=name, priority=priority, direction=direction, access=access, protocol=protocol, source_port_range=source_port_range, destination_port_range=destination_port_range, source_address_prefix=source_address_prefix, destination_address_prefix=destination_address_prefix, resource_group_name=resource_group_name, network_security_group_name=network_security_group_name)