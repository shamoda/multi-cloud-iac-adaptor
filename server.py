import logging
from flask import Flask, request, current_app
from cdktf import App
from main import MyStack
from app.utils import execution_util
from app.utils import file_system_util

app = Flask(__name__)
# logging config
logging.basicConfig(filename='app.log', level=logging.DEBUG, format=f'%(asctime)s %(levelname)s %(name)s %(threadName)s : %(message)s')


@app.route('/synth', methods=['POST'])
def synth():
    app = App()
    stack_name = request.get_json().get('stackName')
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
    current_app.logger.info(stack_name+' destroyed')
    return stack_name+' destroyed'


@app.route('/show/<stack_name>', methods=['GET'])
def show(stack_name):
    return execution_util.Execution_Util().command_executor(stack_name, ["terraform", "show"])


if (__name__ == '__main__'):
    app.run()