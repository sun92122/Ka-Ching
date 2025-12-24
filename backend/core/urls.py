from django.contrib import admin
from django.urls import path
from ninja import NinjaAPI
from accounting.api import router as accounting_router

api = NinjaAPI(title="Ka-Ching API")

# 將 accounting app 的路由掛載上去
api.add_router("/accounting/", accounting_router)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", api.urls),
]
