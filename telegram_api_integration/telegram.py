import requests
from requests import Response


class TelegramClient:

    def __init__(self, telegram_chat_id: int, bot_token: str) -> None:
        self.__telegram_chat_id = telegram_chat_id
        self.__token = bot_token

    def send_message(self, message: str) -> Response:
        url = f"https://api.telegram.org/bot{self.__token}/sendMessage?chat_id={self.__telegram_chat_id}&text={message}"
        return requests.get(url)

    def send_audio(self, audio, title = 'file'):
        payload = {
            'chat_id': self.__telegram_chat_id,
            'title': title,
            'parse_mode': 'HTML'
        }
        files = {
            'audio': audio.read(),
        }
        url = f"https://api.telegram.org/bot{self.__token}/sendAudio"
        return requests.post(
            url,
            data=payload,
            files=files
        )
