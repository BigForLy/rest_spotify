from django.urls import path

from authentication import views

urlpatterns = [
    path('tg/', views.AuthTelegram.as_view()),
]
