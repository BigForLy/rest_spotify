from django.views import generic
from django.conf import settings
from django.http import JsonResponse
from song_download_api_integration.downloader import DownloadStrategy
from spotify_api_integration.my_spotify import Song
from telegram_api_integration import TelegramClient
from .models import Releases, DataFromSpotify, Artists
from spotify_api_integration import MySpotify
from django.views.generic.base import View
from requests import Response


class HomePageView(generic.TemplateView):
    template_name = "all_song.html"

    def get_context_data(self, **kwargs):

        # import redis
        # r = redis.Redis(host='redis-18045.c124.us-central1-1.gce.cloud.redislabs.com',
        #                 port=18045,
        #                 password='WJWHltvrSY4OtwkyogwIx9iDLjildkXv')
        # r.set('r', 'm')
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


class BookDetailView(generic.DetailView):
    """Generic class-based detail view for a book."""
    template_name = "song_detail.html"
    model = Releases
    context_object_name = 'release'


class SongSendMessageView(View):

    def post(self, request):
        if request.META.get('HTTP_X_REQUESTED_WITH') != 'XMLHttpRequest':
            return JsonResponse({'status': 'Not AJAX request'}, status=404)

        if request.user.is_authenticated:
            downloader = DownloadStrategy.music(
                request.POST.get("type"),
                request.POST.get("release")
            )
            song: Song = downloader.download()
            with song as audio:
                result: Response = TelegramClient(request.user.telegram_chat_id, settings.BOT_TOKEN) \
                    .send_audio(audio, f'{song.artist} - {song.name}')

            return JsonResponse({'status': result.reason}, status=result.status_code)
        else:
            return JsonResponse({'status': 'Please login'}, status=401)
