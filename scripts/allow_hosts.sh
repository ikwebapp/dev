#!/bin/bash

# Usage:
# ./update_allowed_hosts.sh 203.0.113.25

SETTINGS_FILE="$HOME/ikweb/ikweb/settings.py"
#SETTINGS_FILE="/home/webadmin/ikweb/ikweb/settings.py"

if [ -z "$1" ]; then
    echo "Error: No IP address provided."
    echo "Usage: $0 <IP_ADDRESS>"
    exit 1
fi

IP="127.0.0.1"

# Replace the ALLOWED_HOSTS line
sed -i "s/^ALLOWED_HOSTS = .*/ALLOWED_HOSTS = [\"$IP\",\"iksaan.com\"]/" "$SETTINGS_FILE"

echo "ALLOWED_HOSTS updated to: $IP"

