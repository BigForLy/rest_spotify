from datetime import datetime
from django.db import models


class DataFromSpotifyInstance(models.Model):
    time_loading = models.DateTimeField('time_loading')

    class Meta:
        ordering = ['id']

    @property
    def is_overdue(self):
        time_now = datetime.now()
        if (time_now-self.time_loading.replace(tzinfo=None)).days > 0 or \
                ((time_now-self.time_loading.replace(tzinfo=None)).seconds > 3600 and time_now.hour == 0):
            return True
        else:
            return False


class ArtistsInstance(models.Model):
    """
    Model of artists
    """
    id = models.CharField('spotify id', primary_key=True,
                          max_length=22, unique=True)
    name = models.TextField(max_length=255)


class ImagesInstance(models.Model):
    url64 = models.URLField('url 64x64', blank=False)
    url300 = models.URLField('url 300x300', blank=False)
    url640 = models.URLField('url 640x640', blank=False)


class ReleasesInstance(models.Model):
    id = models.CharField('spotify id', primary_key=True,
                          max_length=22, unique=True)
    name = models.CharField('name', max_length=255)
    type = models.CharField('single/album', max_length=255)
    images = models.ManyToManyField(ImagesInstance)
    release_date = models.DateField(null=True, blank=True)
    total_track = models.IntegerField(
        'if album - count track, if single - 1', null=True)
    artists = models.ManyToManyField(ArtistsInstance)

    class Meta:
        ordering = ['-release_date']

    @property
    def get_artists(self):
        return ', '.join(artist.name for artist in self.artists.all())
        
    @property
    def get_url64(self):
        return self.images.first().url64
    
    @property
    def get_url640(self):
        return self.images.first().url640
