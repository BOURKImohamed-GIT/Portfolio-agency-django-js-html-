from django.contrib import admin
from django.urls import path,include,re_path
from django.conf.urls import include,url
from django.conf import settings
from django.views.static import serve
from django.conf.urls.static import static
from django.contrib.sitemaps.views import sitemap
from bourki.sitemaps import StaticViewSitemap
from django.contrib.sitemaps import GenericSitemap
from django.contrib.sites.models import  Site
from  django.conf.urls import  handler500
sitemaps ={
    'sitemap':StaticViewSitemap
}
urlpatterns = [
    path('jet/',include("jet.urls")),
    path('jet/dashboard/', include('jet.dashboard.urls', 'jet-dashboard')),
    path('admin/', admin.site.urls),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    path('',include("bourki.urls")),
    re_path(r'^media/(?P<path>.*)$',serve,{'document_root':settings.MEDIA_ROOT,}),
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps},name='django.contrib.sitemaps.views.sitemap')
 ]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

handler404 = "bourki.views.error_404"

handler504 = "bourki.views.error_500"
