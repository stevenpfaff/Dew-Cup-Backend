# Generated by Django 3.2.8 on 2021-11-14 04:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tournament', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tourney',
            name='players',
        ),
    ]