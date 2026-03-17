#!/bin/bash

echo "Starting Movie System"

python bot.py &

uvicorn api.server:app --host 0.0.0.0 --port $PORT
