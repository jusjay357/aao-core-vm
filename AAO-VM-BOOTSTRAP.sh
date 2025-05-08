#!/bin/bash

echo "=== AAO PHASE 7 CORE INSTALL START ==="

# Update system
sudo apt update && sudo apt upgrade -y

# Install dependencies
sudo apt install git unzip curl screen python3-pip -y

# Create AAO directories
mkdir -p ~/aao/logs
mkdir -p ~/aao/drive_sync
touch ~/aao/status.json

# Set up dummy status for now
echo '{"status":"starting","time":"'$(date)'"}' > ~/aao/status.json

# Confirm bootstrap complete
echo "AAO core files installed."
echo "Drive sync and config.json will be added shortly."
echo "Visit ~/aao/status.json for live status."

echo "=== AAO INSTALL COMPLETE ==="
