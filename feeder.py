from flask import Flask
from env import *

app = Flask(__name__)


@app.route('/')
def hello():
    return 'Hello, World!'

@app.route('/feed')
def feed():
    return 'OK ! I drop some food.'