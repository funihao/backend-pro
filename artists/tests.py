from django.test import TestCase
from .models import Artist
from tracks.models import Track
from albums.models import Album


# Create your tests here.
class TestArtists(TestCase):

    def setUp(self):
        self.artist = Artist.objects.create(first_name='david',
                                            last_name='bowie')
        self.album = Album.objects.create(title='heroes',
                                          artist=self.artist)
        self.track = Track.objects.create(title='heroes',
                                          order='0',
                                          track_file='media/tracks/tema',
                                          album=self.album,
                                          artist=self.artist)

    def test_existe(self):
        res = self.client.get('/artists/%d/' % self.artist.id)
        self.assertEqual(res.status_code, 200)
        self.assertTrue('david bowie' in res.content)

    def test_usuario_logueado(self):
        res = self.client.get('/tracks/%s/' % self.track.title)
        self.assertEqual(res.status_code, 302)

    def test_no_existe(self):
        id_viejo = self.artist.id
        self.artist.delete()
        res = self.client.get('/artists/%d/' % id_viejo)
        self.assertEqual(res.status_code, 404)
