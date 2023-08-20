from flask import request
from constructs import Construct
from app.module_processors.aws import aws_security_group_processor, aws_security_group_rule_processor
from app.module_processors.azure import azure_network_security_group_processor, azure_network_security_rule_processor
from app.mappers import module_dependency_mapper

class Json_To_Module_Mapper():
    def __init__(self):
        pass

    def get_modules(self, scope: Construct, request: request):
        terraform_modules = []

        for module in request.get_json().get('modules'):
            if (module.get('moduleType') == 'security-group'):
                aws_security_group = aws_security_group_processor.Aws_Security_Group_Processor().get_aws_security_group(scope=scope, module_json=module)
                terraform_modules.append(aws_security_group)
            elif (module.get('moduleType') == 'security-group-rule'):
                aws_security_group_rule = aws_security_group_rule_processor.Aws_Security_Group_Rule_Processor().get_aws_security_group_rule(scope=scope, module_json=module)
                terraform_modules.append(aws_security_group_rule)
            elif (module.get('moduleType') == 'network-security-group'):
                azure_network_security_group = azure_network_security_group_processor.Azure_Network_Security_Group_Processor().get_azure_network_security_group(scope=scope, module_json=module)
                terraform_modules.append(azure_network_security_group)
            elif (module.get('moduleType') == 'network-security-rule'):
                azure_network_security_rule = azure_network_security_rule_processor.Azure_Network_Security_Rule_Processor().get_azure_network_security_rule(scope=scope, module_json=module)
                terraform_modules.append(azure_network_security_rule)
        # TODO: return terraform_modules with its dependencies
        module_dependency_mapper.Module_Dependency_Mapper().map_terraform_module_dependencies(terraform_modules)