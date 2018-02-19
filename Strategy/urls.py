from django.conf.urls import url, include
from django.contrib import admin

# Strategy app views
from Strategy.views import listing


urlpatterns = [
    # strategy listing
    url(r'^$', listing),
    # strategy listing with condiction categories
    url(r'^(\w+)/$', listing, name='category_url'),
    # strategy listing with condiction categories and level
    url(r'^(\w+)/(\w+)/$', listing, name='listing_url'),
]
