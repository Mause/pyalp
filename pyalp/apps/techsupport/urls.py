from django.conf.urls import patterns, url

from . import views
from pyalp.utils import redirect

urlpatterns = patterns(
    '',

    url(r'^$', views.TechSupportRequestView.as_view()),
    url(r'^details/(\d+)$', views.details, name='techsupport-details')
)


legacy_patterns = patterns(
    '',
    # these are here to rewrite urls from the original alp urls
    url(r'^techsupport\.php$', redirect('/techsupport')),
    url(r'^techsupport_details\.php$', redirect('/techsupport/details'))
)
