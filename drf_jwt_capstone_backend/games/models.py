from django.db import models
from django.contrib.auth import get_user_model
User = get_user_model()
# Create your models here.
class Game(models.Model):
    home_team = models.CharField(max_length=50)
    home_score = models.IntegerField()
    away_team = models.CharField(max_length=50)
    away_score = models.IntegerField()
