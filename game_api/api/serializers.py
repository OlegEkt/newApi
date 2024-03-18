from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from .models import Game, GameUser




class GameUserSerializer(ModelSerializer):

    class Meta:
        model = GameUser
        fields = '__all__'


class GameSerializer(ModelSerializer):
    stage_end_date = serializers.DateField(format='%d.%m.%Y')
    game_user = GameUserSerializer(many=True, read_only=True)

    class Meta:
        model = Game
        fields = '__all__'
        # fields = ('id', 'stage_end_date', 'game_user')