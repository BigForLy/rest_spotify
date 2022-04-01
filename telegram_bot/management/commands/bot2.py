from django.core.management.base import BaseCommand
from telegram import Bot, Update
from telegram.ext import Updater, MessageHandler, Filters, CallbackContext
from telegram.utils.request import Request

from rest_spotify import settings


class Command(BaseCommand):
    help = 'Closes the specified poll for voting'

    def handle(self, *args, **options):
        pass
