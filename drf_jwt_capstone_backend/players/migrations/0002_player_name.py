# Generated by Django 3.2.8 on 2021-11-03 18:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('players', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='player',
            name='name',
            field=models.CharField(default=2, max_length=25),
            preserve_default=False,
        ),
    ]
