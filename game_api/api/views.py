import time

from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404
from rest_framework.views import APIView
from .models import Game, GameUser
from django.core.cache import cache
from .serializers import GameUserSerializer, GameSerializer
from rest_framework import  status
from rest_framework.response import Response
import json

CACHE_TIME = 60 * 60 * 2

class GameListAPIView(APIView):

    def get(self, request):
        data = cache.get_or_set('games_list', Game.objects.all(), CACHE_TIME)
        time.sleep(1)
        return JsonResponse(GameSerializer(data, many=True).data, safe=False)

    def post(self, request):
        time.sleep(2)
        serializer = GameSerializer(data=request.data)
        if serializer.is_valid():
            cache.delete('games_list')
            serializer.save()
            return JsonResponse(serializer.data, status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_400_BAD_REQUEST)


class GameUserListApiView(APIView):

    def get(self, request):
        data = cache.get_or_set('game_users', GameUser.objects.all(), CACHE_TIME)
        return JsonResponse(GameUserSerializer(data, many=True).data, safe=False)


    def post(self, request):
        serializer = GameUserSerializer(data=request.data)
        if serializer.is_valid():
            cache.delete('game_users')
            serializer.save()
            return JsonResponse(json.dumps({"message": 'user created'}), status=status.HTTP_201_CREATED, safe=False)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class GameDetail(APIView):

    def get(self, request, pk):
        game = get_object_or_404(Game, pk=pk)
        data = cache.get_or_set(f'game_{pk}', game, CACHE_TIME)
        return JsonResponse(GameSerializer(data).data, safe=False)

    def put(self,request, pk):
        game = get_object_or_404(Game, pk=pk)
        serializer = GameSerializer(game, data=request.data)
        if serializer.is_valid():
            cache.delete(f'game_{pk}')
            serializer.save()
            return JsonResponse(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):  # Добавляем метод delete
        game = get_object_or_404(Game, pk=pk)
        game.delete()
        cache.delete(f'game_{pk}')
        return JsonResponse({"message": "Game deleted successfully."}, status=status.HTTP_204_NO_CONTENT)

class GameUserDetail(APIView):

    def get(self, request, pk):
        user = get_object_or_404(GameUser, pk=pk)
        data = cache.get_or_set(f'user_{pk}', user, CACHE_TIME)
        return JsonResponse(GameUserSerializer(data).data, safe=False)


    def put(self, request, pk):
        user = get_object_or_404(GameUser, pk=pk)
        serializer = GameUserSerializer(user, data=request.data)
        if serializer.is_valid():
            cache.delete(f'user_{pk}')
            serializer.save()
            return JsonResponse(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self,request, pk):
        user = get_object_or_404(GameUser, pk=pk)
        user.delete()
        cache.delete(f'user_{pk}')
        return JsonResponse({"message": "User deleted successfully."}, status=status.HTTP_204_NO_CONTENT)