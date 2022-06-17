from .abstract_spotify import AbstractSpotify
import requests


class MySpotify(AbstractSpotify):

    def __init__(self):
        super().__init__()
        self._headers = {
            'Accept': 'application/json',
            'Content-Type': 'application/json',
            'Authorization': 'Bearer %s' % self.token
        }
        self._url = 'https://api.spotify.com/v1/browse/new-releases?limit=50'

    def get_new_releases(self):
        result = self._requests(self._url)
        return result

    def _requests(self, url):
        response = requests.get(url=url, headers=self._headers)
        response_json = response.json()
        result = response_json.get('albums').get('items')
        if response_json.get('albums').get('next'):
            result += self._requests(response_json.get('albums').get('next'))
        return result
