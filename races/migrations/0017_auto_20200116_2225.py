# Generated by Django 2.2.7 on 2020-01-16 20:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('races', '0016_auto_20200115_2307'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='race',
            name='base_stake',
        ),
        migrations.AddField(
            model_name='race',
            name='min_stake',
            field=models.FloatField(default=3),
        ),
    ]
