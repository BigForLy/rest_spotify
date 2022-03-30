import base64
import requests

from rest_spotify.settings import env


class Spotify:

    def __init__(self):
        self._token = None

    @property
    def token(self):
        self._token_is_valid()
        return self._token

    def _get_bearer_token(self):
        client_id = env('SPOTYFI_CLIENT_ID')
        secret_key = env('SPOTYFI_SECRET_KEY')
        TOKEN_URL = 'https://accounts.spotify.com/api/token'
        auth_header = base64.urlsafe_b64encode((client_id + ':' + secret_key).encode())
        headers = {
            'Content-Type': 'application/x-www-form-urlencoded',
            'Authorization': 'Basic %s' % auth_header.decode('ascii')
        }
        payload = {
            'grant_type': 'client_credentials',
            # 'code': auth_code,
            # 'redirect_uri': 'https://open.spotify.com/collection/playlists',
        }
        access_token_request = requests.post(url=TOKEN_URL, data=payload, headers=headers)

        access_token_response_data = access_token_request.json()
        print(access_token_response_data)
        self._token = access_token_response_data['access_token']

    def _token_is_valid(self):
        self._get_bearer_token()  # temporary implementation
