from django.db import models
from django.contrib.auth import get_user_model
User = get_user_model()
# Create your models here.
class Game(models.Model):
    game = models.CharField(max_length=50)
    type = models.CharField(max_length=50)
    home_team = models.CharField(max_length=50)
    home_score = models.IntegerField()
    home_players = models.CharField(max_length=100)
    away_team = models.CharField(max_length=50)
    away_score = models.IntegerField()
    away_players = models.CharField(max_length=100)
