# Generated by Django 2.2.7 on 2020-01-28 18:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bets', '0021_auto_20200128_2052'),
    ]

    operations = [
        migrations.AddField(
            model_name='stake',
            name='status_won',
            field=models.CharField(choices=[('True', 'True'), ('False', 'False')], default='None', max_length=10),
        ),
    ]
