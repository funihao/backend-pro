from albums.models import Album
from django.views.generic import ListView, DetailView
#from django.shortcuts import render


class AlbumListView(ListView):
    model = Album
    template_name = 'album_list.html'
    paginate_by = 25

    def get_queryset(self):
        if self.kwargs.get('artist'):
            queryset = self.model.objects.filter(artist__first_name__contains=self.kwargs['artist'])
        else:
            queryset = super(AlbumListView, self).get_queryset()

        return queryset


class AlbumDetailView(DetailView):
    model = Album
    template_name = 'album_detail.html'

