from song.models import Artists, Releases


class ReleasesInstance:

    def __init__(self):
        self.model = Releases

    def create(self):
        pass

    def get(self):
        pass

    def get_all(self):
        return Releases.objects.prefetch_related('artists')

    def update(self):
        pass

    @property
    def count(self) -> int:
        return self.model.objects.all().count()

    def create_or_update_many(self, releases):
        for item in releases:
            release, created = self.model.objects.get_or_create(
                id=item.get('id'),
            )
            release.name = item.get('name')
            release.type = item.get('album_type')
            # release.images = item.get('name')
            release.release_date = item.get('release_date')
            release.total_track = item.get('total_track')
            release.save()
            for artist_item in item['artists']:
                artist = ArtistsInstance().create_or_update(artist_item)
                release.artists.add(artist)
            release.save()

    def delete(self, pk=None):
        self.model.objects.all().delete()


class ArtistsInstance:

    def __init__(self):
        self.model = Artists

    def create(self):
        pass

    def get(self):
        pass

    def update(self):
        pass

    def create_or_update(self, data):
        artist, created = self.model.objects.get_or_create(
            id=data.get('id')
        )
        artist.name = data.get('name')
        artist.save()
        return artist

    def delete(self):
        pass
