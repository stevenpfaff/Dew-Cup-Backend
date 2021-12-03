from rest_framework import serializers
from .models import Game
class GameSerialzer(serializers.ModelSerializer):
    class Meta:
        model = Game
        fields = [ 'home_team', 'home_score', 'away_team', 'away_score']