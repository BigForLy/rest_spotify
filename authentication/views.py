from django.shortcuts import render, redirect

# Create your views here.
from rest_framework.views import APIView

from authentication.models import TelegramUser
from authentication.utils import HashCheck
from rest_spotify import settings


class AuthTelegram(APIView):

    def get(self, request):
        bot_token = settings.BOT_TOKEN
        secret = bot_token.encode('utf-8')
        if not HashCheck(request.GET, secret).check_hash():
            return render(request, 'error.html', {
                'msg': 'Bad hash!'
            })
        user, created = TelegramUser.objects.get_or_create(
            tg_id=request.GET.get('id'),
            )
        user.username=request.GET.get('username'),
        user.photo_url=request.GET.get('photo_url'),
        user.auth_date=request.GET.get('auth_date')
        user.save()
        request.session['user_id'] = user.id
        return redirect('/')
