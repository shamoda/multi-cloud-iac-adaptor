from flask import Flask, request
from cdktf import App
from main import MyStack

app = Flask(__name__)

@app.route('/synth', methods=['POST'])
def home():
    app = App()
    stack_name = request.get_json().get('stackName')
    MyStack(app, stack_name, request)
    app.synth()
    return 'Synth completed'

if (__name__ == '__main__'):
    app.run()