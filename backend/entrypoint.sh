#!/bin/sh
set -e

echo "Waiting for database..."
# 簡單等待 DB 啟動 (正式環境建議用更嚴謹的檢查腳本)
sleep 5

echo "Running Migrations..."
# 自動將我們定義的 Models 同步到資料庫
python manage.py migrate

echo "Initializing System Configs..."
python manage.py init_nginx_conf || echo "Failed to init nginx conf"

echo "Collecting Static Files..."
# 收集 Django Admin 的 CSS/JS 檔
python manage.py collectstatic --noinput

echo "Starting Gunicorn..."
# 啟動 Server (加入 --reload 支援開發時的熱重載)
exec gunicorn core.wsgi:application --bind 0.0.0.0:8000 --reload