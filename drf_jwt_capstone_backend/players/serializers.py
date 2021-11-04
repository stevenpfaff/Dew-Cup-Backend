from rest_framework import serializers
from .models import Player
class PlayerSerialzer(serializers.ModelSerializer):
    class Meta:
        model = Player
        fields = ['id', 'name', 'games_played', 'goals', 'assists', 'info']