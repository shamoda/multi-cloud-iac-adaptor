from imports import security_group_rule
from imports import network_security_rule
from app.mappers.dependency_mappers import aws_security_group_rule_dependency_mapper, azure_network_security_rule_dependency_mapper
from app.const.common_const import DEPENDENCY_IDENTIFIER, AWS_SECURITY_GROUP_ID_IDENTIFIER, AZURE_NETWORK_SECURITY_GROUP_NAME_IDENTIFIER

class Module_Dependency_Mapper():
    def __init__(self):
        pass

    def map_terraform_module_dependencies(self, terraform_modules):
        for module in terraform_modules:
            if (isinstance(module, security_group_rule.SecurityGroupRule)):
                if DEPENDENCY_IDENTIFIER in module.security_group_id:
                    aws_security_group_rule_dependency_mapper.Aws_Security_Group_Rule_Dependency_Mapper().map_aws_security_group_rule_properties(terraform_modules.index(module), module.security_group_id.split('.')[0], AWS_SECURITY_GROUP_ID_IDENTIFIER, terraform_modules)
            elif (isinstance(module, network_security_rule.NetworkSecurityRule)):
                if DEPENDENCY_IDENTIFIER in module.network_security_group_name:
                    azure_network_security_rule_dependency_mapper.Azure_Security_Rule_Dependency_Mapper().map_azure_security_rule_properties(terraform_modules.index(module), module.network_security_group_name.split('.')[0], AZURE_NETWORK_SECURITY_GROUP_NAME_IDENTIFIER, terraform_modules)
        # TODO: return mapped modules
        return terraform_modules