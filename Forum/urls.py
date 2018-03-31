from django.conf.urls import url, include
from django.contrib import admin

from Forum.views import listing, details

urlpatterns = [
    url(r'^$', listing),
    url(r'^(\d+)$', listing, name = 'category-url'),
    url(r'^details/(\d+)$', details, name = 'forum-url'),
]