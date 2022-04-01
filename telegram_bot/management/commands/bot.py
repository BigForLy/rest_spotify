from django.core.management.base import BaseCommand
from telegram import Bot, Update
from telegram.ext import Updater, MessageHandler, Filters, CallbackContext
from telegram.utils.request import Request

from rest_spotify import settings


class Command(BaseCommand):
    help = 'Closes the specified poll for voting'

    def log_errors(self, func):
        def _(*args, **kwargs):
            try:
                return func(*args, **kwargs)
            except Exception as ex:
                self.stdout.write(f'Errors: {str(ex)}', ending='\n')
                raise ex

        return _

    @staticmethod
    def do_echo(update: Update, context: CallbackContext):
        chat_id = update.message.chat_id
        text = update.message.text

        reply_text = f'Your ID \n{chat_id}\n{text}'
        update.message.reply_text(
            text=reply_text,
        )

    def handle(self, *args, **options):
        self.stdout.write("Start handle", ending='\n')
        request = Request(
            connect_timeout=0.5,
            read_timeout=1,
            con_pool_size=10
        )
        bot = Bot(
            request=request,
            token=settings.BOT_TOKEN
        )
        self.stdout.write(str(bot.get_me()))

        updater = Updater(
            bot=bot,
            use_context=True
        )
        message_handler = MessageHandler(
            filters=Filters.text,
            callback=self.do_echo,
            run_async=True
        )
        updater.dispatcher.add_handler(message_handler)
        updater.start_polling()
        updater.idle()
