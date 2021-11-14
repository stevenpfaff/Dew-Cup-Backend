from rest_framework import serializers
from .models import Tourney
class TourneySerialzer(serializers.ModelSerializer):
    class Meta:
        model = Tourney
        fields = ['name', 'teams', 'champions', 'mvp']