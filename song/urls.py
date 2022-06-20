from django.urls import path
from . import views


urlpatterns = [
    path('', views.HomePageView.as_view(), name='song'),
    path('song/send_message/', views.SongSendMessageView.as_view(), name='send_message'),
    path('song/<str:pk>/', views.BookDetailView.as_view(), name='song_detail'),
]
