# Generated by Django 2.2.7 on 2020-01-20 18:25

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('bets', '0012_auto_20200120_2021'),
    ]

    operations = [
        migrations.AddField(
            model_name='stake',
            name='bet_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
