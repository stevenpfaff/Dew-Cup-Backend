# Generated by Django 3.2.8 on 2021-12-05 04:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('games', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='game',
            name='away_players',
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='game',
            name='home_players',
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
    ]