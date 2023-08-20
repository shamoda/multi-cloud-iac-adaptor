from flask import request
from constructs import Construct
from imports import security_group_rule

class Aws_Security_Group_Rule_Processor():
    def __init__(self):
        pass

    def get_aws_security_group_rule(self, scope: Construct, module_json: request):
        tfId = module_json.get('tfId')
        type = module_json.get('type')
        fromPort = module_json.get('fromPort')
        toPort = module_json.get('toPort')
        protocol = module_json.get('protocol')
        cidrBlocks = module_json.get('cidrBlocks')
        securityGroupId = module_json.get('securityGroupId')
        return security_group_rule.SecurityGroupRule(scope, tfId, type=type, from_port=fromPort, to_port=toPort, protocol=protocol, cidr_blocks=cidrBlocks, security_group_id=securityGroupId)