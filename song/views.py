from datetime import datetime
from django.views import generic

from django.views.generic import TemplateView
from song.models import ReleasesInstance

from song.services import DataFromSpotify, Releases
from spotify_api_interaction.my_spotify import MySpotify


class HomePageView(TemplateView):
    template_name = "all_song.html"

    def get_context_data(self, **kwargs):
        dropdown_list = (
            'Show',
            'SendToTelegram'
        )
        context = super().get_context_data(**kwargs)
        last_write = DataFromSpotify.get()
        if last_write is None or last_write.is_overdue:
            new_releases = MySpotify().get_new_releases()  # todo: handle error
            DataFromSpotify.create(datetime.now())
            Releases.delete()
            Releases.create_or_update_many(new_releases)
        context['new_releases'] = Releases.get_all()
        context['dropdown_list'] = dropdown_list
        return context


class BookDetailView(generic.DetailView):
    """Generic class-based detail view for a book."""
    template_name = "song_detail.html"
    model = ReleasesInstance
    context_object_name = 'release'
