from flask import request
from constructs import Construct
from cdktf import LocalBackend

class Backend_Processor():
    def __init__(self):
        pass

    def get_backend(self, scope: Construct, request: request):
        backend_json = request.get_json().get('backend')
        return LocalBackend(scope, path=backend_json.get('path'))