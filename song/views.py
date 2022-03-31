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

from spotify_api_interaction.new_release import NewRelease


class HomePageView(TemplateView):
    template_name = "all_song.html"

    def get_context_data(self, **kwargs):
        dropdown_list = (
            'Show',
            'SendToTelegram'
        )
        context = super().get_context_data(**kwargs)
        new_releases = NewRelease().get()
        context['new_releases'] = new_releases
        context['dropdown_list'] = dropdown_list
        return context
