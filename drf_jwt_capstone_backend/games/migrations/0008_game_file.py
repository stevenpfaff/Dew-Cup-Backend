# Generated by Django 3.2.8 on 2021-12-07 20:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('games', '0007_remove_game_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='game',
            name='file',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
    ]
