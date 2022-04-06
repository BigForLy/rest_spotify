from django.db import models


class Artists(models.Model):
    """
    Model of artists
    """
    id = models.CharField('spotify id', primary_key=True, max_length=22, unique=True)
    name = models.TextField(max_length=255)


class Images(models.Model):
    pass


class Releases(models.Model):
    id = models.CharField('spotify id', primary_key=True, max_length=22, unique=True)
    name = models.CharField('name', max_length=255)
    type = models.CharField('single/album', max_length=255)
    images = models.CharField('in future ForeignKey(Images)', max_length=255, null=True, blank=False, default=None)
    release_date = models.DateField(null=True, blank=True)
    total_track = models.IntegerField('if album - count track, if single - 1', null=True)
    artists = models.ManyToManyField(Artists)

    class Meta:
        ordering = ['-release_date']

    @property
    def get_artists(self):
        return ','.join(artist.name for artist in self.artists.all())
