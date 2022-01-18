from django.contrib import admin
from django.urls import path
from django.urls.conf import include, include
# imagens
from django.conf.urls.static import static
from django.conf import settings
# robots
from django.views.generic import TemplateView
from django.contrib.sitemaps.views import sitemap
from core.sitemaps import StaticViewSitemap
sitemaps = {
    'static': StaticViewSitemap
}
urlpatterns = [
    path('', include('core.urls')),
    path('admin/', admin.site.urls),
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps}),
    # robots
    path(
        "robots.txt",
        TemplateView . as_view(template_name="robots.txt",
                               content_type="text/plain"),
    ),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
