from flask import Flask
from env import *

app = Flask(__name__)


@app.route('/')
def hello():
    return 'Hello, World!'

@app.route('/feed')
def hello():
    return 'OK ! I drop some food.'

if __name__ == '__main__':
   app.run(debug=True, port=port, host=host)