# Generated by Django 3.2.8 on 2021-12-05 04:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('games', '0002_auto_20211204_2232'),
    ]

    operations = [
        migrations.AlterField(
            model_name='game',
            name='away_players',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='game',
            name='home_players',
            field=models.CharField(max_length=100),
        ),
    ]
