# Generated by Django 3.0 on 2019-12-09 07:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('races', '0007_auto_20191208_2250'),
    ]

    operations = [
        migrations.AddField(
            model_name='future_races',
            name='race_name',
            field=models.CharField(default=0, max_length=120),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='past_races',
            name='race_name',
            field=models.CharField(default=0, max_length=120),
            preserve_default=False,
        ),
    ]
