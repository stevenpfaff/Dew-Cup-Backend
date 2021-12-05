from django.db import models
from django.contrib.auth import get_user_model
User = get_user_model()

class Tourney(models.Model):
    name = models.CharField(max_length=25)
    teams = models.CharField(max_length=500)
    players = models.CharField(max_length=500)
    champions = models.CharField(max_length=25)
    mvp = models.CharField(max_length=25)

