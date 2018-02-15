from django.conf.urls import url, include
from django.contrib import admin

# Users app views
from . import views


urlpatterns = [
    url(r'^$', views.index),
]
