from flask import request
from constructs import Construct
from imports import security_group

class Aws_Security_Group_Processor():
    def __init__(self):
        pass

    def get_aws_security_group(self, scope: Construct, module_json: request):
        tfId = module_json.get('tfId')
        name = module_json.get('name')
        return security_group.SecurityGroup(scope, tfId, name=name)