from django.db import models
from django.contrib.auth import get_user_model
User = get_user_model()
# Create your models here.
class Player(models.Model):
    player = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=25)
    games_played = models.IntegerField()
    goals = models.IntegerField()
    assists = models.IntegerField()
    info = models.CharField(max_length=500)
    is_captain = models.BooleanField(default=False)