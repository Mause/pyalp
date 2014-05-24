from django.conf.urls import patterns, url
from django.shortcuts import redirect as redirect_func
# from django.core.urlresolvers import reverse
from django.conf import settings

from accounts import views
from pyalp.utils import redirect

urlpatterns = patterns(
    '',

    url(r'^login/?$', views.login_view, name='accounts-login'),
    url(r'^logout/?$', views.logout_view, name='accounts-logout'),
    url(r'^users$', views.users, name='accounts-users'),
    url(
        r'^users/(?P<user_id>\d+)$',
        views.single_user,
        name='accounts-single-user'
    ),
    # url(r'^register$', views.register, name='accounts-register'),
)

legacy_patterns = patterns(
    '',
    url(r'^users\.php$', redirect('/accounts/users')),
    url(r'^login\.php$', redirect(settings.LOGIN_URL)),
    url(r'^logout\.php$', redirect(settings.LOGOUT_URL)),
    url(
        r'^disp_users\.php$',
        lambda request: redirect_func(
            'accounts-single-user-username',
            request.GET['id']
        )
    ),
    url(r'^chng_userinfo\.php$', redirect('/accounts/profile/change'))
)
