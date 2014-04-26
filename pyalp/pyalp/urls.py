from django.conf import settings
from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.admindocs import urls as admindocs_urls

admin.autodiscover()

urlpatterns = patterns(
    '',
    url(r'^$', include('common.urls', app_name='global')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^admindocs/', include(admindocs_urls)),
    url(r'^pizza/', include('pizza.urls', app_name='pizza')),
    url(r'^tournaments/', include('tournaments.urls', app_name='tournaments')),
    url(r'^flags/', include('flags.urls', app_name='flags'))
)

# load in the legacy url rewrites
import importlib
for app in settings.INSTALLED_APPS:
    try:
        urls = importlib.import_module(app + '.urls')
    except ImportError:
        pass
    else:
        if hasattr(urls, 'legacy_patterns'):
            urlpatterns += getattr(urls, 'legacy_patterns')

if settings.DEBUG:
    import debug_toolbar
    urlpatterns += patterns(
        '',
        url(r'^__debug__/', include(debug_toolbar.urls)),
    )

# add the static files
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
