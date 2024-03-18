from django.urls import path
from .views import GameListAPIView, GameDetail, GameUserDetail, GameUserListApiView

urlpatterns = [
    path('games/', GameListAPIView.as_view(), name='games_list'),
    path('games/<int:pk>/', GameDetail.as_view(), name='game_detail'),
    path('game_users/', GameUserListApiView.as_view(), name='game_users'),
    path('game_users/<int:pk>/', GameUserDetail.as_view(), name='users_detail')
]
