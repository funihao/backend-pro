from django.conf.urls import patterns, url
from albums.views import AlbumListView, AlbumDetailView


urlpatterns = patterns('',
    url(r'^albums/$', AlbumListView.as_view(), name='album_list'),
    url(r'^albums/(?P<artist>[\w\-]+)/$', AlbumListView.as_view(), name='album_list'),
    url(r'^albums/detail/(?P<id>[\w\-]+)/$', AlbumDetailView.as_view(), name='album_detail'),
)
