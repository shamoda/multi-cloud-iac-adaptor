from flask import request, current_app, jsonify
from app.utils.db_util import db
from bson import json_util, ObjectId
import json

class Stack_Service():
    def __init__(self):
        pass

    def insert_config(self, request: request, version: int):
        try: 
            data = {
                'stack_name': request.get_json().get('stackName'),
                'version': version,
                'status': 'applied',
                'config': request.get_json()
            }

            db_response = db.stacks.insert_one(data)
            current_app.logger.info('Stack updated: ' + str(db_response.inserted_id))

        except Exception as ex:
            current_app.logger.error(ex)


    def latest_identical_stack_exists(self, request: request):
        try:
            latest_stack = self.get_latest_version(request.get_json().get('stackName'))
            if latest_stack == None:
                return False
            elif latest_stack['config'] == request.get_json():
                return True

        except Exception as ex:
            current_app.logger.error(ex)


    def get_latest_version(self, stack_name: str):
        try:
            stacks = list(db.stacks.find({"stack_name": stack_name}))
            if len(stacks) == 0:
                return None
            else:
                latest_version = stacks[0]
                for stack in stacks:
                    if stack['version'] > latest_version['version']:
                        latest_version = stack
                return latest_version

        except Exception as ex:
            current_app.logger.error(ex)


    def mark_as_destroyed(self, stack_name: str):
        try:
            latest_stack = self.get_latest_version(stack_name)
            db.stacks.update_one({'_id':latest_stack['_id']}, {"$set": {'status':'destroyed'}})
            current_app.logger.info('Stack destroyed: ' + stack_name)
            
        except Exception as ex:
            current_app.logger.error(ex)


    def get_stacks_by_name(self, stack_name: str):
        try:
            stacks = list(db.stacks.find({"stack_name": stack_name}))
            return json.loads(json_util.dumps(stacks))
        except Exception as ex:
            current_app.logger.error(ex)
            return str(ex)


    def get_stacks_by_id(self, stack_id: str):
        try:
            stack = db.stacks.find_one({"_id": ObjectId(stack_id)})
            return json.loads(json_util.dumps(stack))
        except Exception as ex:
            current_app.logger.error(ex)
            return str(ex)