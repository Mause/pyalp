from django.conf.urls import patterns, url

from . import views
from pyalp.utils import redirect

urlpatterns = patterns(
    '',

    url(r'^$', views.pizza),
    url(r'^list$', views.pizza_list),

    # these are going to be implemented in the Django admin interface
    url(r'^admin/pizza$', redirect('/admin/pizza/pizzaorder')),
    url(r'^chng_pizza$', redirect('/admin/pizza/pizza'))
    url(
        r'^admin/pizza_list/$',
        redirect('/admin/pizza/pizzaorder/order_summary/')
    )
)


legacy_patterns = patterns(
    '',
    # these are here to rewrite urls from the original mod_pizza
    url(r'^admin_pizza\.php$', redirect('/admin/pizza/pizzaorder')),
    url(r'^chng_pizza\.php$', redirect('/admin/pizza/pizza')),

    url(r'^admin_pizza_list\.php$', redirect('/pizza/admin/pizza_list')),
    url(r'^pizza\.php$', redirect('/pizza/')),
    url(r'^pizza_list\.php$', redirect('/pizza/list'))
)
