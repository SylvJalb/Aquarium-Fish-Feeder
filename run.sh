export FLASK_APP=feeder
export FLASK_RUN_PORT=4500
export FLASK_RUN_HOST=0.0.0.0
/home/pi/.local/bin/gunicorn -w 2 -b $FLASK_RUN_HOST:$FLASK_RUN_PORT $FLASK_APP:app