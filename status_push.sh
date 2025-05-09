#!/bin/bash

# Set this to the full path of your signal.json inside the public directory
TARGET_PATH=~/aao-core-vm/public/status/signal.json

# Check argument
if [ -z "$1" ]; then
  echo "Usage: ./status_push.sh [buy|sell|close|standby]"
  exit 1
fi

# Create/update the signal file
echo "{\"signal\": \"$1\"}" > $TARGET_PATH

# Confirm
echo "Signal pushed: $1"
cat $TARGET_PATH
