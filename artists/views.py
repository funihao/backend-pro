from .models import Artist
from django.views.generic.detail import DetailView
#from django.shortcuts import render


class ArtistDetailView(DetailView):
    model = Artist
    context_object_name = 'artist'

    def get_template_names(self):
        return 'artist.html'
