# Generated by Django 3.2.8 on 2021-11-14 17:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('players', '0008_alter_player_profile_picture'),
    ]

    operations = [
        migrations.AlterField(
            model_name='player',
            name='profile_picture',
            field=models.ImageField(upload_to=''),
        ),
    ]
