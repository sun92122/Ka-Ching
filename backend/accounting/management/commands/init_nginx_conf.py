from django.core.management.base import BaseCommand
from accounting.models import SystemSetting
from accounting.services import generate_nginx_conf


class Command(BaseCommand):
    help = "Initialize Nginx configuration based on SystemSetting"

    def handle(self, *args, **options):
        try:
            # 讀取系統設定
            settings = SystemSetting.load()

            # 生成設定檔
            if generate_nginx_conf(settings.allowed_domains):
                self.stdout.write(
                    self.style.SUCCESS("Successfully generated nginx default.conf")
                )
            else:
                self.stdout.write(self.style.ERROR("Failed to generate nginx config"))

        except Exception as e:
            self.stdout.write(self.style.ERROR(f"Error initializing nginx conf: {e}"))
