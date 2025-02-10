

from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('admin-tenants/', admin.site.urls),
]
