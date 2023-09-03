from flask import current_app
import shutil
import os

class File_System_Util():
    def __init__(self):
        pass

    def remove_directory(self, stack_name : str):
        STACK_DIR = os.path.abspath(os.path.join(os.path.dirname( __file__ ), '..', '..', 'cdktf.out', 'stacks', stack_name))
        try:
            shutil.rmtree(STACK_DIR)
            current_app.logger.info(stack_name + " directory removed")
        except OSError as o:
            current_app.logger.info(f"Error, {o.strerror}: {STACK_DIR}")
