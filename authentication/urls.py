from django.urls import path

from authentication import views

urlpatterns = [
    path('success/', views.AuthTelegram.as_view()),
]
