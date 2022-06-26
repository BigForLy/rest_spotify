from datetime import datetime
from django.db import models
from django.db.models.manager import BaseManager
from typing import Any


class DataFromSpotify(models.Model):

    time_loading = models.DateTimeField(
        'time_loading',
        auto_now_add=True
    )

    class Meta:
        db_table = 'data_from_spotify'
        ordering = ['id']

    @property
    def is_overdue(self):
        time_now = datetime.now()
        if (time_now-self.time_loading.replace(tzinfo=None)).days > 0 or \
                ((time_now-self.time_loading.replace(tzinfo=None)).seconds > 3600 and time_now.hour == 0):
            return True
        else:
            return False


class ArtistsManager(models.Manager):

    def create_or_update_from_data(self, data):
        artist, _ = Artists.objects.get_or_create(
            id=data.get('id')
        )
        artist.name = data.get('name')
        artist.save()
        return artist


class Artists(models.Model):
    """
    Model of artists
    """

    id = models.CharField(
        'spotify id',
        primary_key=True,
        max_length=22,
        unique=True
    )
    name = models.TextField(max_length=255)

    objects: BaseManager[Any] = ArtistsManager()

    class Meta:
        db_table = 'artists'


class ImagesManager(models.Manager):

    def create_from_data(self, data):
        return Images.objects.create(
            url64=data[2].get('url'),
            url300=data[1].get('url'),
            url640=data[0].get('url')
        )


class Images(models.Model):

    url64 = models.URLField(
        'url 64x64',
        blank=False
    )
    url300 = models.URLField(
        'url 300x300',
        blank=False
    )
    url640 = models.URLField(
        'url 640x640',
        blank=False
    )

    objects: BaseManager[Any] = ImagesManager()

    class Meta:
        db_table = 'images'


class ReleasesManager(models.Manager):

    def create_from_data(self, data):
        for item in data:
            release, _ = Releases.objects.get_or_create(
                id=item.get('id'),
                images=Images.objects.create_from_data(item.get('images'))
            )
            release.name = item.get('name')
            release.type = item.get('type')  #todo: create new attribute item.get('album_type')
            release.release_date = item.get('release_date')
            release.total_track = item.get('total_tracks')
            for artist_item in item['artists']:
                artist = Artists.objects.create_or_update_from_data(
                    artist_item
                )
                release.artists.add(artist)
            release.save()


class Releases(models.Model):

    id = models.CharField(
        'spotify id',
        primary_key=True,
        max_length=22,
        unique=True
    )
    name = models.CharField(
        'name',
        max_length=255
    )
    type = models.CharField(
        'single/album',
        max_length=255
    )
    images = models.ForeignKey(
        Images,
        on_delete=models.CASCADE
    )
    release_date = models.DateField(
        null=True,
        blank=True
    )
    total_track = models.IntegerField(
        'if album - count track, if single - 1',
        null=True
    )
    artists = models.ManyToManyField(
        Artists
    )

    objects: BaseManager[Any] = ReleasesManager()

    class Meta:
        db_table = 'releases'
        ordering = ['-release_date']

    @property
    def get_artists(self):
        return ', '.join(artist.name for artist in self.artists.all())

    @property
    def get_url64(self):
        return self.images.url64

    @property
    def get_url640(self):
        return self.images.url640
