import os

from django.views.generic import TemplateView

# class Homepage(APIView):
#     http_method_names = ['get', 'put', 'patch', 'delete', 'head', 'options', 'trace']
#
#     def get(self, request):
#         return render(
#             request,
#             'base_generic.html',
#         )


# class HomePageView(TemplateView):
#
#     template_name = "base_generic.html"
#
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         return context
# from django.conf import settings
# from django.http import HttpResponse
from django.shortcuts import render, redirect

#
# from django_telegram_login.widgets.constants import (
#     SMALL,
#     MEDIUM,
#     LARGE,
#     DISABLE_USER_PHOTO,
# )
# from django_telegram_login.widgets.generator import (
#     create_callback_login_widget,
#     create_redirect_login_widget,
# )
# from django_telegram_login.authentication import verify_telegram_authentication
# from django_telegram_login.errors import (
#     NotTelegramDataError,
#     TelegramDataIsOutdatedError,
# )
#
# bot_name = settings.TELEGRAM_BOT_NAME
# bot_token = settings.TELEGRAM_BOT_TOKEN
# redirect_url = settings.TELEGRAM_LOGIN_REDIRECT_URL
#
# from django_telegram_login.authentication import verify_telegram_authentication
# from django_telegram_login.errors import (
#     NotTelegramDataError,
#     TelegramDataIsOutdatedError,
# )
#
#
# def index(request):
#     # Initially, the index page may have no get params in URL
#     # For example, if it is a home page, a user should be redirected from the widget
#     if not request.GET.get('hash'):
#         return HttpResponse('Handle the missing Telegram data in the response.')
#
#     try:
#         result = verify_telegram_authentication(bot_token=bot_token, request_data=request.GET)
#
#     except TelegramDataIsOutdatedError:
#         return HttpResponse('Authentication was received more than a day ago.')
#
#     except NotTelegramDataError:
#         return HttpResponse('The data is not related to Telegram!')
#
#     # Or handle it as you wish. For instance, save to the database.
#     return HttpResponse('Hello, ' + result['first_name'] + '!')
#
#
# def callback(request):
#     telegram_login_widget = create_callback_login_widget(bot_name, size=SMALL)
#
#     context = {'telegram_login_widget': telegram_login_widget}
#     return render(request, 'callback.html', context)
#
#
# def redirect(request):
#     telegram_login_widget = create_redirect_login_widget(
#         redirect_url, bot_name, size=LARGE, user_photo=DISABLE_USER_PHOTO
#     )
#
#     context = {'telegram_login_widget': telegram_login_widget}
#     return render(request, 'redirect.html', context)
from authentication.utils import HashCheck


def register(request):
    secret = os.getenv('BOT_TOKEN').encode('utf-8')
    if not HashCheck(request.GET, secret).check_hash():
        return render(request, 'error.html', {
            'msg': 'Bad hash!'
        })
    # user = TgUser.make_from_dict(request.GET)
    # user.save()
    # request.session['user_id'] = user.id
    return redirect('/')
