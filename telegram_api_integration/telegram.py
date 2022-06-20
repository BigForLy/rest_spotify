import requests
from requests import Response
import os


class TelegramClient:

    def __init__(self, telegram_chat_id: int) -> None:
        self.__telegram_chat_id = telegram_chat_id
        self.__token = os.getenv('BOT_TOKEN')

    def send_message(self, message:str) -> Response:
        url = f"https://api.telegram.org/bot{self.__token}/sendMessage?chat_id={self.__telegram_chat_id}&text={message}"
        response = requests.get(url)
        return response
