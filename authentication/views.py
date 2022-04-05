from django.contrib.auth import login
from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect
from authentication.models import User
from authentication.utils import HashCheck
from rest_spotify import settings


class LoginTelegram(LoginView):

    def get(self, request, *args, **kwargs):
        bot_token = settings.BOT_TOKEN
        secret = bot_token.encode('utf-8')
        if not HashCheck(request.GET, secret).check_hash():
            return render(request, 'error.html', {
                'msg': 'Bad hash!'
            })
        user, created = User.objects.get_or_create(
            telegram_chat_id=request.GET.get('id'),
        )
        if user.username:
            user.username = request.GET.get('username')
        else:
            user.username = f'User_{user.telegram_chat_id}'
        user.photo_url = request.GET.get('photo_url')
        user.auth_date = request.GET.get('auth_date')
        user.save()
        login(request, user)
        return redirect('song')
