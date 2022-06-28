from django.views import generic
from django.conf import settings
from django.http import JsonResponse
from song.tasks import celery_send_song
from .models import Releases, DataFromSpotify, Artists
from spotify_api_integration import MySpotify
from django.views.generic.base import View


class HomePageView(generic.TemplateView):
    template_name = "all_song.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        last_write = DataFromSpotify.objects.last()
        if last_write is None or last_write.is_overdue:
            new_releases = MySpotify().get_new_releases()
            DataFromSpotify.objects.create()
            Releases.objects.all().delete()
            Artists.objects.all().delete()
            Releases.objects.create_from_data(new_releases)
        context['new_releases'] = Releases.objects\
            .prefetch_related('artists', 'images')
        return context


class SongDetailView(generic.DetailView):
    template_name = "song_detail.html"
    model = Releases
    context_object_name = 'release'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        subreleases = MySpotify().get_subreleases(kwargs.get('object').pk)  # todo: cache
        context['subreleases'] = subreleases
        return context


class SongSendMessageView(View):

    def post(self, request):
        if request.META.get('HTTP_X_REQUESTED_WITH') != 'XMLHttpRequest':
            return JsonResponse({'status': 'Not AJAX request'}, status=404)

        if request.user.is_authenticated:
            celery_send_song.delay(telegram_chat_id=request.user.telegram_chat_id,
                                   bot_token=settings.BOT_TOKEN,
                                   release_type=request.POST.get("type"),
                                   release_pk=request.POST.get("release"))

            return JsonResponse({'status': 'OK'}, status=200)
        else:
            return JsonResponse({'status': 'Please login'}, status=401)
