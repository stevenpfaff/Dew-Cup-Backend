from django.db import models
from django.contrib.auth import get_user_model
User = get_user_model()
# Create your models here.
class Player(models.Model):
    name = models.CharField(max_length=25)
    games_played = models.IntegerField()
    goals = models.IntegerField()
    assists = models.IntegerField()
    info = models.CharField(max_length=500)
    file = models.TextField()
    minibat_games_played = models.IntegerField()
    at_bats = models.IntegerField()
    hits = models.IntegerField()
    homeruns = models.IntegerField()
    batting_average = models.IntegerField()