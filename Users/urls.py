from django.conf.urls import url, include
from django.contrib import admin

# Users app views
from . import views


urlpatterns = [
    # login url
    url(r'^login/$', views.login),
    # logout url
    url(r'^logout/$', views.logout),
]
