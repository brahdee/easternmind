from django.contrib import admin
from django.urls import include, path
from django.conf.urls.static import static
from pictures.conf import get_settings
from . import settings

from main import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.main, name='main'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if get_settings().USE_PLACEHOLDERS:
    urlpatterns += [path("_pictures/", include("pictures.urls"))]
