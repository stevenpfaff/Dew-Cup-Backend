# Generated by Django 3.2.8 on 2021-12-15 16:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('players', '0015_auto_20211203_1540'),
    ]

    operations = [
        migrations.AddField(
            model_name='player',
            name='assists',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='player',
            name='goals',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
