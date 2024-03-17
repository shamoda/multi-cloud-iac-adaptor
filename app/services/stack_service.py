from flask import request, current_app, jsonify
from app.utils.db_util import db
from bson import json_util, ObjectId
import json
from app.utils import crypto_util

class Stack_Service():
    def __init__(self):
        pass

    def insert_config(self, request: request, version: int):
        try: 
            data = {
                'stack_name': request.get_json().get('stackName'),
                'version': version,
                'status': 'applied',
                'config': crypto_util.Crypto_Util().encrypt_message(str(request.get_json()).replace("\'", "\""))
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
            elif crypto_util.Crypto_Util().decrypt_message(latest_stack['config']) == str(request.get_json()):
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
            decrypted_stacks = []
            for stack in stacks:
                decrypted_stacks.append(self.decrypted_stack(stack))
            return json.loads(json_util.dumps(decrypted_stacks))
        except Exception as ex:
            current_app.logger.error(ex)
            return str(ex)


    def get_stacks_by_id(self, stack_id: str):
        try:
            stack = db.stacks.find_one({"_id": ObjectId(stack_id)})
            return json.loads(json_util.dumps(self.decrypted_stack(stack)))
        except Exception as ex:
            current_app.logger.error(ex)
            return str(ex)
        
    def get_all_stacks(self):
        try:
            stacks = list(db.stacks.find())
            stack_names = []
            distinct_stacks = []
            for stack in stacks:
                if stack['stack_name'] in stack_names:
                    continue
                distinct_stacks.append(json.loads(json_util.dumps(self.decrypted_stack(self.get_latest_version(stack['stack_name'])))))
                stack_names.append(stack['stack_name'])
            return distinct_stacks
        except Exception as ex:
            current_app.logger.error(ex)
            return str(ex)
        
        
    def decrypted_stack(self, encrypted_stack):
        data = {
                    '_id': encrypted_stack['_id'],
                    'stack_name': encrypted_stack['stack_name'],
                    'version': encrypted_stack['version'],
                    'status': encrypted_stack['status'],
                    'config': json.loads(crypto_util.Crypto_Util().decrypt_message(encrypted_stack['config']))
                }
        return json.loads(json_util.dumps(data))