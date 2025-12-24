import os

# Nginx 設定檔的共享路徑 (對應 compose.yaml 的 volume)
NGINX_SHARED_PATH = "/app/nginx_shared/default.conf"


def generate_nginx_conf(allowed_domains: list):
    """
    生成 Nginx 設定檔並寫入共享 Volume。
    Nginx 容器的看門狗會偵測此檔案變更並自動 Reload。
    """
    # 如果白名單為空，預設允許 localhost，避免完全鎖死
    if not allowed_domains:
        allowed_domains = ["localhost:8080", "127.0.0.1:8080"]

    server_names = " ".join(allowed_domains)

    # Nginx 設定模板
    # 設定 8080 port 轉發 (對應 gunicorn 聽的 port)
    conf_content = f"""
server {{
    listen 80;
    server_name {server_names};

    # 前端靜態檔
    location / {{
        root /usr/share/nginx/html;
        index index.html;
        try_files $uri $uri/ /index.html;
    }}

    # 媒體檔案 (上傳的圖片等)
    location /media/ {{
        alias /usr/share/nginx/html/media/;
    }}

    # 後端 API 轉發
    location /api/ {{
        proxy_pass http://backend:8000;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
    }}

    # Django Admin 後台 (需要獨立處理靜態檔)
    location /admin/ {{
        proxy_pass http://backend:8000;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
    }}

    # Django Admin 的靜態檔案 (CSS/JS)
    location /static/ {{
        alias /app/static/; 
    }}
}}
"""
    try:
        # 確保目錄存在
        os.makedirs(os.path.dirname(NGINX_SHARED_PATH), exist_ok=True)
        # 寫入檔案
        with open(NGINX_SHARED_PATH, "w") as f:
            f.write(conf_content)
        return True
    except Exception as e:
        print(f"Failed to write nginx conf: {e}")
        return False
