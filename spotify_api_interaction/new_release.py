from spotify_api_interaction.autorisation import Spotify
import requests


class NewRelease(Spotify):

    def __init__(self):
        super().__init__()
        self._headers = {
            'Accept': 'application/json',
            'Content-Type': 'application/json',
            'Authorization': 'Bearer %s' % self.token
        }
        # self._url = 'https://api.spotify.com/v1/browse/new-releases?offset=80&limit=20'
        self._url = 'https://api.spotify.com/v1/browse/new-releases'

    def get(self):
        response = requests.get(url=self._url, headers=self._headers)
        result = response.json().get('albums').get('items')
        print(result)
        return result
