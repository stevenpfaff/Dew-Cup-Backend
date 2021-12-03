from django.db import models
from django.contrib.auth import get_user_model
User = get_user_model()
# Create your models here.
class Team(models.Model):
    name = models.CharField(max_length=25)
    wins = models.IntegerField()
    losses = models.IntegerField()
    goals = models.IntegerField()
    goals_against = models.IntegerField()
    championships = models.IntegerField()
    players = models.CharField(max_length=100)
    file = models.TextField()
    runs = models.IntegerField()
    runs_against = models.IntegerField()
    homeruns = models.IntegerField()
    batting_average = models.DecimalField(max_digits=3, decimal_places=3)
    
