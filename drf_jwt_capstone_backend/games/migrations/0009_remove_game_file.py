# Generated by Django 3.2.8 on 2021-12-07 21:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('games', '0008_game_file'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='game',
            name='file',
        ),
    ]
