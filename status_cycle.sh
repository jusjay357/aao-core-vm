#!/bin/bash

# Cycles through AAO signals and updates signal.json every second
# Loop: buy → sell → close → standby → repeat

TARGET_PATH=~/aao-core-vm/public/status/signal.json
SIGNALS=("buy" "sell" "close" "standby")

while true; do
  for signal in "${SIGNALS[@]}"; do
    echo "{\"signal\": \"$signal\"}" > "$TARGET_PATH"
    echo "[Cycle] Signal pushed: $signal"
    sleep 1
  done
done
