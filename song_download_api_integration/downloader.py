from abc import ABC, abstractmethod
from song_download_api_integration.youtube_search import Youtube
from spotify_api_integration.my_spotify import MySpotify, Song


class AbstractDownloader(ABC):

    def __init__(self) -> None:
        self.__url: str = 'https://api.spotify.com/v1/'

    @property
    def url(self) -> str:
        return self.__url

    @abstractmethod
    def download(self) -> Song:
        pass


class DownloadTrack(AbstractDownloader):

    def __init__(self, music_id) -> None:
        super().__init__()
        self.__modify = 'tracks/'
        self.__music_id = music_id

    def download(self) -> Song:
        """
        return song path
        """
        song: Song = MySpotify().get_info_about_song(self.url)
        results = Youtube(track_name=song.name, artist=song.artist).search()
        for result in results:
            if self.__comparison_time_duration(song.duration, result['duration']):
                youtube_url = f'https://www.youtube.com/{result["url_suffix"]}'
                song.path = Youtube.download(youtube_url)
                return song

    def __comparison_time_duration(self, duration: int, youtube_song_duration: str) -> bool:
        """
        duration in ms, youtube_song_duration format 'm:s'
        """
        minute, sec = map(int, youtube_song_duration.split(':'))
        youtube_song_duration_in_ms = (minute * 60 + sec)*1_000
        if youtube_song_duration_in_ms - 2 * 1_000 <= duration <= youtube_song_duration_in_ms + 2 * 1_000:
            return True
        return False

    @property
    def url(self) -> str:
        return f'{super().url}{self.__modify}{self.__music_id}'


class DownloadAlbum(AbstractDownloader):

    def __init__(self) -> None:
        super().__init__()
        self.__modify = 'album/'


class DownloadStrategy:

    @classmethod
    def music(cls, type_, music_id) -> AbstractDownloader:
        if type_ == 'single':
            strategy = DownloadTrack(music_id)
        else:
            raise

        return cls(strategy)

    def __init__(self, strategy) -> None:
        self.__strategy: AbstractDownloader = strategy

    def download(self) -> str:
        """
        return path song
        """
        return self.__strategy.download()
