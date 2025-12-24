#!/bin/sh

CONF_FILE="/etc/nginx/conf.d/default.conf"
CURRENT_HASH=""

# 使用 "daemon off;" 確保 PID 是真正的主行程
echo "Starting Nginx..."
nginx -g "daemon off;" &
NGINX_PID=$!

# 確保 PID 存在
sleep 1

echo "Starting Nginx Config Watchdog..."

while true; do
    # 1. 檢查設定檔是否存在
    if [ -f "$CONF_FILE" ]; then
        # 2. 計算 Hash
        NEW_HASH=$(md5sum "$CONF_FILE" | awk '{print $1}')
        
        # 3. 若 Hash 改變 (且不是第一次啟動)
        if [ "$CURRENT_HASH" != "" ] && [ "$NEW_HASH" != "$CURRENT_HASH" ]; then
            echo "Configuration changed. Reloading Nginx..."
            
            # 檢查新設定檔語法是否正確
            nginx -t
            if [ $? -eq 0 ]; then
                nginx -s reload
                echo "Nginx reloaded successfully."
            else
                echo "ERROR: New configuration is invalid! Not reloading."
            fi
        fi
        
        CURRENT_HASH="$NEW_HASH"
    else
        # 為了避免 log 刷屏，只有在第一次等待時印出，或每隔幾次印出（這裡保持簡單）
        echo "Waiting for config file at $CONF_FILE..."
    fi

    # 檢查 Nginx 是否還活著
    if ! kill -0 $NGINX_PID 2>/dev/null; then
        echo "Nginx process has stopped. Exiting."
        exit 1
    fi

    # 每 3 秒檢查一次
    sleep 3
done