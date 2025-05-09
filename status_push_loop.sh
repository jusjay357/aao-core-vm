#!/bin/bash

# Looping AAO signal broadcaster
# Usage: ./status_push_loop.sh [buy|sell|close|standby]

TARGET_PATH=~/aao-core-vm/public/status/signal.json

if [ -z "$1" ]; then
  echo "Usage: ./status_push_loop.sh [buy|sell|close|standby]"
  exit 1
fi

while true; do
  echo "{\"signal\": \"$1\"}" > $TARGET_PATH
  echo "[Loop] Signal pushed: $1"
  sleep 1
done
