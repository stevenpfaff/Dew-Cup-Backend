from rest_framework import serializers
from .models import Team
class TeamSerialzer(serializers.ModelSerializer):
    class Meta:
        model = Team
        fields = ['name', 'wins', 'losses', 'goals', 'goals_against', 'championships', 'players']