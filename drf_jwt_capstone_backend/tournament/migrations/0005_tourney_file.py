# Generated by Django 3.2.8 on 2021-12-06 18:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tournament', '0004_remove_tourney_players'),
    ]

    operations = [
        migrations.AddField(
            model_name='tourney',
            name='file',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
    ]
