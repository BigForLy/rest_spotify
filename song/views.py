from django.views import generic

from django.views.generic import TemplateView
from .models import Releases, DataFromSpotify, Artists
from spotify_api_interaction import MySpotify


class HomePageView(TemplateView):
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
        dropdown_list = (
            'Show',
            'SendToTelegram'
        )
        context['dropdown_list'] = dropdown_list
        return context


class BookDetailView(generic.DetailView):
    """Generic class-based detail view for a book."""
    template_name = "song_detail.html"
    model = Releases
    context_object_name = 'release'
