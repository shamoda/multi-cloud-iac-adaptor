#!/usr/bin/env python
from constructs import Construct
from cdktf import App, TerraformStack
from flask import request
from app.module_processors import backend_processor, provider_processor
from app.mappers import json_to_module_mapper


class MyStack(TerraformStack):
    def __init__(self, scope: Construct, id: str, param: request):
        super().__init__(scope, id)

        # define resources here
        backend_processor.Backend_Processor().get_backend(scope=self, request=request)
        provider_processor.Provider_Processor().get_provider(scope=self, request=request)
        json_to_module_mapper.Json_To_Module_Mapper().get_modules(scope=self, request=request)


# app = App()
# MyStack(app, "Multi Cloud IAC Adaptor")

# app.synth()
