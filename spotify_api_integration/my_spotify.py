from dataclasses import dataclass
from .abstract_spotify import AbstractSpotify
import requests
import os


@dataclass
class Song:
    name: str
    artist: str
    duration: int
    path: str

    def __enter__(self):
        self.file = open(self.path, 'rb') 
        return self.file

    def __exit__(self, type, value, traceback):
        self.file.close()
        os.remove(self.path)


class MySpotify(AbstractSpotify):

    def __init__(self):
        super().__init__()
        self.__headers = {
            'Accept': 'application/json',
            'Content-Type': 'application/json',
            'Authorization': 'Bearer %s' % self.token
        }

    def get_new_releases(self) -> dict:
        url = 'https://api.spotify.com/v1/browse/new-releases?limit=50'
        response_json = self.__requests(url)
        result = response_json.get('albums').get('items')
        if response_json.get('albums').get('next'):
            result += self.__requests(response_json.get('albums').get('next'))
        return result

    def get_subreleases(self, parent_pk) -> dict:
        url = f'https://api.spotify.com/v1/albums/{parent_pk}'
        response_json = self.__requests(url)
        return response_json.get('tracks').get('items')

    def get_info_about_song(self, url) -> Song:
        response_json = self.__requests(url)
        return Song(
            response_json['name'],
            response_json['artists'][0]['name'],
            response_json['duration_ms'],
            ""
        )

    def __requests(self, url) -> dict:
        response = requests.get(url=url, headers=self.__headers)
        return response.json()
