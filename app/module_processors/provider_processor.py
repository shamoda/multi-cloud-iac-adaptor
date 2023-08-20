from flask import request
from constructs import Construct
from cdktf_cdktf_provider_aws import provider as aws_provider
from cdktf_cdktf_provider_azurerm import provider as azure_provider

class Provider_Processor():
    def __init__(self):
        pass

    def get_provider(self, scope: Construct, request: request):
        provider_json = request.get_json().get('provider')
        if (provider_json.get('type') == 'aws'):
            return aws_provider.AwsProvider(scope, provider_json.get('tfId'), region=provider_json.get('region'))
        elif (provider_json.get('type') == 'azure'):
            return azure_provider.AzurermProvider(scope, provider_json.get('tfId'), features={})