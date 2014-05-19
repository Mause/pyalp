from pyalp.utils import redirect
from django.conf.urls import patterns, url

from . import views

urlpatterns = patterns(
    '',

    url(r'^$', views.TournamentsView.as_view()),
)

legacy_patterns = patterns(
    '',

    # these are here to rewrite urls from the originals from alp
    url(r'^tournaments\.php$', redirect('/tournaments/'))
)
