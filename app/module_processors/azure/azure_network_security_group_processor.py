from flask import request
from constructs import Construct
from imports import network_security_group

class Azure_Network_Security_Group_Processor():
    def __init__(self):
        pass

    def get_azure_network_security_group(self, scope: Construct, module_json: request):
        tfId = module_json.get('tfId')
        name = module_json.get('name')
        location = module_json.get('location')
        resourceGroupName = module_json.get('resourceGroupName')
        return network_security_group.NetworkSecurityGroup(scope, tfId, name=name, location=location, resource_group_name=resourceGroupName);