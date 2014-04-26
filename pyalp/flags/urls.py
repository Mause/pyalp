from django.conf.urls import patterns, url

from flags import views

urlpatterns = patterns(
    '',
    url(r'^$', views.AdminToggleView.as_view(), name='index'),
)
