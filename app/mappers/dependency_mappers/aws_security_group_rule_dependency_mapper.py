from imports import security_group
from app.const.common_const import AWS_SECURITY_GROUP_ID_IDENTIFIER

class Aws_Security_Group_Rule_Dependency_Mapper():
    def __init__(self):
        pass

    def map_aws_security_group_rule_properties(self, target_index, source_tf_id, property_type, terraform_modules):
        # iterating through all the TF modules
        for module in terraform_modules:

            # getting the source TF module with specified tfId
            if (module.friendly_unique_id == source_tf_id):

                # getting the exact module type of source module
                ########## AWS Security Group ##########
                if (isinstance(module, security_group.SecurityGroup)):
                    # checking which target property has the dependency
                    if (property_type == AWS_SECURITY_GROUP_ID_IDENTIFIER):
                        # evaluating the incoming output identifier with all the outputs of AWS Security Group module
                        if (AWS_SECURITY_GROUP_ID_IDENTIFIER in terraform_modules[target_index].security_group_id):
                            terraform_modules[target_index].security_group_id = module.id_output
        return terraform_modules
                
            