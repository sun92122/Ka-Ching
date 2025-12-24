#!/bin/sh

CONFIG_FILE="/etc/cloudflared/config/tunnel_token"

echo "Starting Cloudflared Watchdog..."

while true; do
    if [ -f "$CONFIG_FILE" ]; then
        echo "Token found! Starting Tunnel..."
        TOKEN=$(cat "$CONFIG_FILE")
        
        # 啟動 Tunnel (這會佔用主程序)
        exec cloudflared tunnel --no-autoupdate run --token "$TOKEN"
    else
        echo "Waiting for Tunnel Token at $CONFIG_FILE..."
    fi
    sleep 5
done