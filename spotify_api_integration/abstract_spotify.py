import base64
import requests
import redis
from rest_spotify.settings import env


class AbstractSpotify:

    @property
    def token(self):
        return self._get_token()

    def __create_token(self) -> dict:
        auth_header = base64.urlsafe_b64encode(
            (env('SPOTYFI_CLIENT_ID') + ':' + env('SPOTYFI_SECRET_KEY')).encode()
        )
        headers = {
            'Content-Type': 'application/x-www-form-urlencoded',
            'Authorization': 'Basic %s' % auth_header.decode('ascii')
        }
        payload = {
            'grant_type': 'client_credentials'
        }

        access_token_request = requests.post(
            url='https://accounts.spotify.com/api/token',
            data=payload,
            headers=headers
        )
        token_data = access_token_request.json()
        print(token_data)
        return token_data

    def _get_token(self) -> str:
        redis_client = redis.Redis(
            host=env('REDIS_HOST'),
            port=env('REDIS_PORT'),
            password=env('REDIS_PASSWORD')
        )
        spotify_token: bytes | None = redis_client.get('spotify_token')
        if spotify_token:
            return spotify_token.decode('utf-8')
        token_data = self.__create_token()
        redis_client.setex('spotify_token', token_data['expires_in'], token_data['access_token'])
        return token_data['access_token']
