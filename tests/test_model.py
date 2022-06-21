from unittest import TestCase
from telegram_api_integration import TelegramClient
from dotenv import load_dotenv
import os


class TestSendTelegramMessageText(TestCase):

    def test_incorrect(self):
        telegram_chat_id = 1
        message = 1
        bot_token = 1
        result = TelegramClient(telegram_chat_id,  bot_token) \
            .send_message(message)
        self.assertEqual(result.status_code, 404)

    def test_correctly(self):
        load_dotenv()
        telegram_chat_id = os.getenv('ADMIN_TELEGRAM_CHAT_ID')
        message = 'test message'
        bot_token = os.getenv('BOT_TOKEN')
        result = TelegramClient(telegram_chat_id,  bot_token) \
            .send_message(message)
        self.assertEqual(result.status_code, 200)


class TestSendTelegramMessageSound(TestCase):

    def test_incorrect(self):
        telegram_chat_id = 1
        bot_token = 1
        with open('tests/test_sound.mp3', 'rb') as audio:
            result = TelegramClient(telegram_chat_id,  bot_token) \
                .send_audio(audio)
        self.assertEqual(result.status_code, 404)

    def test_correctly(self):
        load_dotenv()
        telegram_chat_id = os.getenv('ADMIN_TELEGRAM_CHAT_ID')
        bot_token = os.getenv('BOT_TOKEN')

        with open('tests/test_song.mp3', 'rb') as audio:
            result = TelegramClient(telegram_chat_id,  bot_token) \
                .send_audio(audio)
        self.assertEqual(result.status_code, 200)
