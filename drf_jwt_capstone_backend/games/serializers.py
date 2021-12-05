from rest_framework import serializers
from .models import Game
class GameSerialzer(serializers.ModelSerializer):
    class Meta:
        model = Game
        fields = [ 'game', 'home_team', 'home_score', 'home_players', 'away_team', 'away_score', 'away_players']