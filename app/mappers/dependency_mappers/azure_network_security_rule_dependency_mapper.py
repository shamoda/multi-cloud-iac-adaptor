from imports import network_security_group
from app.const.common_const import AZURE_NETWORK_SECURITY_GROUP_NAME_IDENTIFIER

class Azure_Security_Rule_Dependency_Mapper():
    def __init__(self):
        pass

    def map_azure_security_rule_properties(self, target_index, source_tf_id, property_type, terraform_modules):
        # iterating through all the TF modules
        for module in terraform_modules:

            # getting the source TF module with specified tfId
            if (module.friendly_unique_id == source_tf_id):

                # getting the exact module type of source module
                ########## Azure Network Security Group ##########
                if (isinstance(module, network_security_group.NetworkSecurityGroup)):
                    # checking which target property has the dependency
                    if (property_type == AZURE_NETWORK_SECURITY_GROUP_NAME_IDENTIFIER):
                        # evaluating the incoming output identifier with all the outputs of Azure Network Security Group module
                        if (AZURE_NETWORK_SECURITY_GROUP_NAME_IDENTIFIER in terraform_modules[target_index].network_security_group_name):
                            terraform_modules[target_index].network_security_group_name = module.name_output
        return terraform_modules