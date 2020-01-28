# Generated by Django 2.2.7 on 2019-12-08 20:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('races', '0006_past_races_jackpot'),
    ]

    operations = [
        migrations.AddField(
            model_name='future_races',
            name='drivers',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='future_races',
            name='stakes',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='past_races',
            name='drivers',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='past_races',
            name='stakes',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]