# Generated by Django 3.2.8 on 2021-11-11 16:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('players', '0004_remove_player_is_captain'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='player',
            name='player',
        ),
    ]
