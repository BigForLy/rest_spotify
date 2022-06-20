from django.contrib.auth import login
from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect
from authentication.models import User
from authentication.utils import HashCheck
from rest_spotify import settings

from django.contrib.auth import logout
from django.shortcuts import redirect


class LoginTelegram(LoginView):

    def get(self, request, *args, **kwargs):
        bot_token = settings.BOT_TOKEN
        secret = bot_token.encode('utf-8')
        if request.GET.get('hash') is None:
            return redirect('song')
        if not HashCheck(request.GET, secret).check_hash():
            return render(request, 'error.html', {
                'msg': 'Bad hash!'
            })
        user, _ = User.objects.get_or_create(
            telegram_chat_id=int(request.GET.get('id')),
        )
        if request.GET.get('username'):
            user.username = request.GET.get('username')
        else:
            user.username = f'User_{user.telegram_chat_id}'
        user.photo_url = request.GET.get('photo_url')
        user.auth_date = request.GET.get('auth_date')
        user.save()
        login(request, user)
        return redirect('song')

def logout_view(request):
    logout(request)
    return redirect('song')
