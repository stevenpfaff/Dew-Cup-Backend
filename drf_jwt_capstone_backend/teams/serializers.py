from rest_framework import serializers
from .models import Team
class TeamSerialzer(serializers.ModelSerializer):
    class Meta:
        model = Team
        fields = ['id', 'name', 'wins', 'losses', 'championships', 'players']