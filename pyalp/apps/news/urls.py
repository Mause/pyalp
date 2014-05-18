from django.conf.urls import patterns, url

from pizza import views
from pyalp.utils import redirect

urlpatterns = patterns(
    '',

    url(r'^$', views.pizza, name='pizza-index')
)


legacy_patterns = patterns(
    '',
    # these are here to rewrite urls from the original mod_pizza
    url(r'^admin_news\.php$', redirect('/admin/news/newsitem')),
)
