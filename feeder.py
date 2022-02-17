from flask import Flask
from env import *

app = Flask(__name__)


@app.route('/')
def hello():
    return 'Hello, World!'

if __name__ == '__main__':
   app.run(debug=True, port=80, host=host)