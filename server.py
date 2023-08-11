from flask import Flask
from cdktf import App

app = Flask(__name__)

@app.route('/', methods=['GET'])
def home():
    app = App()
    return "Hello World!"

if (__name__ == '__main__'):
    app.run()