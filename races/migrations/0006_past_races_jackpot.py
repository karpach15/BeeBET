# Generated by Django 2.2.7 on 2019-12-08 14:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('races', '0005_auto_20191208_1637'),
    ]

    operations = [
        migrations.AddField(
            model_name='past_races',
            name='jackpot',
            field=models.FloatField(default=0),
            preserve_default=False,
        ),
    ]
