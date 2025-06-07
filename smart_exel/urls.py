"""
URL configuration for smart_exel project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path
from .views import index, plantillasexel # Adjusted import for app structure

urlpatterns = [
    path('', index, name='index'),
    path("admin/", admin.site.urls, name='admin'),
    path('plantillasexel/', plantillasexel, name='plantillasexel'),
]

# The following lines are typically used for development (DEBUG=True)
# and are not needed when using WhiteNoise or a dedicated web server for static files in production.
# If you need to serve media files in development with DEBUG=False (not typical for production setup),
# you might need a different approach or ensure your web server handles it.
# from django.conf import settings
# from django.conf.urls.static import static
# if settings.DEBUG: # Or a specific setting to enable this for dev even with DEBUG=False
#     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
#     urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

from django.conf import settings
from django.conf.urls.static import static

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
