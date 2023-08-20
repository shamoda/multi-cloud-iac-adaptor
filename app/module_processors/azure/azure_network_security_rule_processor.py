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
        resourceGroupName = module_json.get('resourceGroupName')
        networkSecurityGroupName = module_json.get('networkSecurityGroupName')
        return network_security_rule.NetworkSecurityRule(scope, tfId, name=name, priority=priority, direction=direction, access=access, protocol=protocol, resource_group_name=resourceGroupName, network_security_group_name=networkSecurityGroupName)