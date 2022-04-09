from django.urls import path

from authentication import views

urlpatterns = [
    path('', views.LoginTelegram.as_view()),
]
