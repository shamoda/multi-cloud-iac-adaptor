from flask import current_app
import os
import subprocess
import re

class Execution_Util():
    def __init__(self):
        pass

    def command_executor(self, stack_name : str, command_args : []):
        EXECUTION_DIR = os.path.abspath(os.path.join(os.path.dirname( __file__ ), '..', '..', 'cdktf.out', 'stacks', stack_name))

        completed_process = subprocess.run(command_args, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, universal_newlines=True, cwd=EXECUTION_DIR)

        # removing ANSI escape sequence
        log = completed_process.stdout
        ansi_escape =re.compile(r'(\x9B|\x1B\[)[0-?]*[ -\/]*[@-~]')
        processed_log = ansi_escape.sub('', log)
        current_app.logger.info(processed_log)
        return processed_log
    

    def command_executor_with_output_file(self, stack_name : str, command_args : []):
        EXECUTION_DIR = os.path.abspath(os.path.join(os.path.dirname( __file__ ), '..', '..', 'cdktf.out', 'stacks', stack_name))

        with open(EXECUTION_DIR+"/plan.json", "w") as output_file:
            subprocess.run(command_args, stdout=output_file, check=True, cwd=EXECUTION_DIR, universal_newlines=True)
            