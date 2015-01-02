from django.conf.urls import patterns, url
from artists.views import ArtistDetailView

urlpatterns = patterns('',
    url(r'^artists/(?P<pk>[\d]+)', ArtistDetailView.as_view()),
)