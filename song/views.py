from django.views import generic
from django.conf import settings
from django.http import JsonResponse
from telegram_api_integration import TelegramClient
from .models import Releases, DataFromSpotify, Artists
from spotify_api_integration import MySpotify
from django.views.generic.base import View
from requests import Response


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
            release = request.POST.get("release")
            result: Response = TelegramClient(request.user.telegram_chat_id, settings.get('BOT_TOKEN')) \
                .send_message(release)
            return JsonResponse({'status': result.reason}, status=result.status_code)
        else:
            return JsonResponse({'status': 'Please login'}, status=401)
