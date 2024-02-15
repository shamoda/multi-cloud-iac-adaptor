import logging
from flask import Flask, request, current_app
from cdktf import App
from main import MyStack
from app.utils import execution_util
from app.utils import file_system_util
from app.services import stack_service

app = Flask(__name__)
# logging config
logging.basicConfig(filename='app.log', level=logging.DEBUG, format=f'%(asctime)s %(levelname)s %(name)s %(threadName)s : %(message)s')


@app.route('/synth', methods=['POST'])
def synth():
    app = App()
    stack_name = request.get_json().get('stackName')

    existing_stack = stack_service.Stack_Service().get_latest_version(stack_name)

    if existing_stack != None:
        if stack_service.Stack_Service().latest_identical_stack_exists(request):
            current_app.logger.info(stack_name+' with same config exists as latest')
        else:
            new_version = existing_stack['version']+1
            stack_service.Stack_Service().insert_config(request, new_version)
            current_app.logger.info('A new version created for the existing stack: '+stack_name)
    else:
        stack_service.Stack_Service().insert_config(request, 1)
        current_app.logger.info('A new stack created: '+stack_name)
    MyStack(app, stack_name, request)
    app.synth()

    execution_util.Execution_Util().command_executor(stack_name, ["terraform", "init"])
    execution_util.Execution_Util().command_executor(stack_name, ["terraform", "apply", "--auto-approve"])
    current_app.logger.info(stack_name+' applied')
    return stack_name+' applied'


@app.route('/destroy/<stack_name>', methods=['DELETE'])
def destroy(stack_name):
    execution_util.Execution_Util().command_executor(stack_name, ["terraform", "destroy", "--auto-approve"])
    file_system_util.File_System_Util().remove_directory(stack_name)
    stack_service.Stack_Service().mark_as_destroyed(stack_name)
    current_app.logger.info(stack_name+' destroyed')
    return stack_name+' destroyed'


@app.route('/show/<stack_name>', methods=['GET'])
def show(stack_name):
    return execution_util.Execution_Util().command_executor(stack_name, ["terraform", "show"])


@app.route('/stacks/<stack_name>', methods=['GET'])
def get_stacks(stack_name):
    return stack_service.Stack_Service().get_stacks_by_name(stack_name)


@app.route('/stacks/id/<stack_id>', methods=['GET'])
def get_stack_by_id(stack_id):
    return stack_service.Stack_Service().get_stacks_by_id(stack_id)


if (__name__ == '__main__'):
    app.run()