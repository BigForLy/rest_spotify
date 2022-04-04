from django.shortcuts import render, redirect

# Create your views here.
from rest_framework.views import APIView

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
        # user = TgUser.make_from_dict(request.GET)
        # user.save()
        # request.session['user_id'] = user.id
        return redirect('/')
