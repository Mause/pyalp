from django.conf.urls import patterns, url

from common import views
from pyalp.utils import redirect

urlpatterns = patterns(
    '',
    url(r'^$', views.index)
)


legacy_patterns = patterns(
    '',
    url(r'^index\.php$', redirect('/')),
    url(r'^users\.php$', redirect('/users'))
)
