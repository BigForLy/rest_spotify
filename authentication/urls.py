from django.urls import path

from authentication import views

urlpatterns = [
    path('success/', views.LoginTelegram.as_view()),
    path('logout/', views.logout_view, name='logout'),
]
