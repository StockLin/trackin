from django.conf.urls import url, include
from django.contrib import admin

from Forum.views import listing
# detail

urlpatterns = [
    url(r'^$', listing),
    url(r'^(\d+)$', listing, name = 'category-url'),
    # url(r'^detail/(\d+)$', views.detail, name = 'forum-url'),
]