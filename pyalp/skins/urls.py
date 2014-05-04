from django.conf.urls import patterns, url
from skins import views

urlpatterns = patterns(
    '',

    url(r'^x\.css$', views.skin_css),
)
