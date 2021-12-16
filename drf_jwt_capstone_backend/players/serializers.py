from rest_framework import serializers
from .models import Player
class PlayerSerialzer(serializers.ModelSerializer):
    class Meta:
        model = Player
        fields = [ 'name', 'games_played', 'goals', 'assists', 'minibat_games_played', 'at_bats', 'hits', 'homeruns', 'batting_average', 'info', 'file']