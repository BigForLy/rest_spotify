from datetime import datetime
from django.shortcuts import render

# def index(request):
#     """
#     Функция отображения для домашней страницы сайта.
#     """
#     # Генерация "количеств" некоторых главных объектов
#     num_books = 1
#     num_instances = 1
#     # Доступные книги (статус = 'a')
#     num_instances_available = 1
#     num_authors = 1  # Метод 'all()' применён по умолчанию.
#
#     # Отрисовка HTML-шаблона index.html с данными внутри
#     # переменной контекста context
#     return render(
#         request,
#         'base_generic.html',
#         context={'num_books': num_books, 'num_instances': num_instances,
#                  'num_instances_available': num_instances_available, 'num_authors': num_authors},
#     )
from django.views.generic import TemplateView

from song.services import ReleasesInstance
from spotify_api_interaction.new_release import MySpotify


class HomePageView(TemplateView):
    template_name = "all_song.html"

    def get_context_data(self, **kwargs):
        dropdown_list = (
            'Show',
            'SendToTelegram'
        )
        context = super().get_context_data(**kwargs)
        ReleasesInstance().delete()
        if ReleasesInstance().count == 0:
            new_releases = MySpotify().get_new_releases()  # todo: handle error
            # create_or_update_releases(new_releases)
            foo = datetime.now()
            ReleasesInstance().create_or_update_many(new_releases)
            bar = datetime.now()
            print('create_or_update_many ', bar-foo)
        context['new_releases'] = ReleasesInstance().get_all()
        context['dropdown_list'] = dropdown_list
        return context
