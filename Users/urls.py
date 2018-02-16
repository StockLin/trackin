from django.conf.urls import url, include
from django.contrib import admin

# Users app views
from . import views


urlpatterns = [
    # login url
    url(r'^login/$', views.login),
    # logout url
    url(r'^logout/$', views.logout),
    # registration
    url(r'^sign_up/', views.sign_up),
    url(r'^activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$', views.activate, name='activate'),
]
