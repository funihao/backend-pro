from django.conf.urls import patterns, url
from tracks.views import track_view

urlpatterns = patterns('',
    url(r'^tracks/(?P<title>[\w\-\W]+)/', 'track_view',
        name='track_view'),
)