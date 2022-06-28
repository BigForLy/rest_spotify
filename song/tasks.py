from rest_spotify.celery import app
from song_download_api_integration.downloader import DownloadStrategy
from spotify_api_integration.my_spotify import Song
from telegram_api_integration.telegram import TelegramClient


@app.task
def celery_send_song(telegram_chat_id: int, bot_token: str, release_type: str, release_pk: str) -> bool:
    downloader = DownloadStrategy.music(
        release_type,
        release_pk
    )
    song: Song = downloader.download()
    with song as audio:
        TelegramClient(telegram_chat_id, bot_token) \
            .send_audio(audio, f'{song.artist} - {song.name}')
