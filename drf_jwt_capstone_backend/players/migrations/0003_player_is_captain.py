# Generated by Django 3.2.8 on 2021-11-05 14:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('players', '0002_player_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='player',
            name='is_captain',
            field=models.BooleanField(default=False),
        ),
    ]
