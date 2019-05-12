from django.contrib import admin
from django.urls import path, include

from apps.api.router import router

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include((router.get_urls(), 'apps.api'), namespace='api')),
]
