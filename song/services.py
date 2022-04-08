from song.models import ArtistsInstance, DataFromSpotifyInstance, ReleasesInstance


class DataFromSpotify:
    """
    CRUD interface DataFromSpotifyInstance
    """

    @staticmethod
    def create(datetime_now):
        release = DataFromSpotifyInstance.objects.create(time_loading=datetime_now)
        release.save()   # todo: rename

    @staticmethod
    def get():
        return DataFromSpotifyInstance.objects.last()

    @staticmethod
    def update():
        pass

    @staticmethod
    def delete():
        DataFromSpotifyInstance.objects.all().delete()


class Releases:

    def create(self):
        pass

    def get(self):
        pass

    @staticmethod
    def get_all():
        return ReleasesInstance.objects.prefetch_related('artists')

    def update(self):
        pass

    @property
    def count(self) -> int:
        return ReleasesInstance.objects.all().count()

    @staticmethod
    def create_or_update_many(releases):
        for item in releases:
            release, _ = ReleasesInstance.objects.get_or_create(
                id=item.get('id'),
            )
            release.name = item.get('name')
            release.type = item.get('album_type')
            # release.images = item.get('name')
            release.release_date = item.get('release_date')
            release.total_track = item.get('total_track')
            release.save()
            for artist_item in item['artists']:
                artist = Artists.create_or_update(artist_item)
                release.artists.add(artist)
            release.save()

    @staticmethod
    def delete():
        ReleasesInstance.objects.all().delete()


class Artists:

    def create(self):
        pass

    def get(self):
        pass

    def update(self):
        pass

    @staticmethod
    def create_or_update(data):
        artist, created = ArtistsInstance.objects.get_or_create(
            id=data.get('id')
        )
        artist.name = data.get('name')
        artist.save()
        return artist

    def delete(self):
        pass
