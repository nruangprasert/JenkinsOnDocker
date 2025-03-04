#!/bin/bash

# Start Jenkins
/usr/local/bin/jenkins.sh &

# Start Flask App
python3 /usr/src/app/app.py &

# Start Ngrok
ngrok http 8080 --log=stdout &

# Keep container running
wait -n