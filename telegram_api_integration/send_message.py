import requests
from requests import Response
import os

def send_message(telegram_chat_id: int, message: str) -> Response:
    TOKEN = os.getenv('BOT_TOKEN')
    text = message
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage?chat_id={telegram_chat_id}&text={text}"
    response = requests.get(url)
    return response