import datetime
import os
from flask import Flask
from flask import request
from pytz import timezone

from env import *

app = Flask(__name__)


@app.route('/')
def hello():
    return 'Hello, World!'

@app.route('/feed', methods=['GET', 'POST'])
def feed():
    log_file = "./feeder.log"
    if request.method == 'GET':
        # Check if the log file exists
        if os.path.isfile(log_file):
            # return content of feeder.log
            with open(log_file, 'r') as f:
                content = f.read()
            # replace newline with <br>
            content = content.replace('\n', '<br>')
            return content
        else:
            return "No log file found."
    if request.method == 'POST':
        when = request.form['feed']
        if when == 'now':
            # feed now
            with open(log_file, 'a') as f:
                # write time without microseconds
                f.write("\n" + str(datetime.datetime.now(timezone(timezone_name)).replace(microsecond=0)))
            return 'OK ! I drop some food...'
    with open(log_file, 'a') as f:
            f.write("\n"  + str(datetime.datetime.now(timezone(timezone_name)).replace(microsecond=0)) + " Problem with the request")
    return 'Problem with your request...'

if __name__ == '__main__':
   app.run(debug = True)