from django.contrib import admin
from django.urls import path
from django.urls.conf import include, include
# imagens
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('', include('core.urls')),
    path('admin/', admin.site.urls),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
