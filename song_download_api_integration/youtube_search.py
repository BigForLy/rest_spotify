from youtube_search import YoutubeSearch
import os
from pytube import YouTube


class Youtube:

    def __init__(self, track_name: str, artist: str) -> None:
        self.__track_name: str = track_name
        self.__artist: str = artist

    def search(self) -> list:
        return list(YoutubeSearch(str(self.__track_name + " " + self.__artist)).to_dict())

    @staticmethod
    def download(link) -> str:
        """
        return song path
        """
        yt = YouTube(link)
        downloaded_file = yt.streams.filter(only_audio=True).first().download()
        base, _ = os.path.splitext(downloaded_file)
        new_file = base + '.mp3'
        os.rename(downloaded_file, new_file)
        return new_file