# Generated by Django 2.2.7 on 2019-12-08 14:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('races', '0003_auto_20191208_1620'),
    ]

    operations = [
        migrations.AlterField(
            model_name='future_races',
            name='distance',
            field=models.IntegerField(max_length=50),
        ),
        migrations.AlterField(
            model_name='past_races',
            name='distance',
            field=models.IntegerField(max_length=50),
        ),
    ]