from django.urls import path
from . import views


urlpatterns = [
    path('', views.HomePageView.as_view(), name='song'),
    path('<str:pk>/', views.BookDetailView.as_view(), name='song_detail')
]
