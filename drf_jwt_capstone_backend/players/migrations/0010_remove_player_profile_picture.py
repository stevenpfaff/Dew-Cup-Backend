# Generated by Django 3.2.8 on 2021-11-14 17:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('players', '0009_alter_player_profile_picture'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='player',
            name='profile_picture',
        ),
    ]
