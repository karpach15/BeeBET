# Generated by Django 3.0 on 2020-02-04 20:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bets', '0022_stake_status_won'),
    ]

    operations = [
        migrations.AddField(
            model_name='stake',
            name='opened',
            field=models.CharField(choices=[('Closed', 'Closed'), ('Open', 'Open')], default='Closed', max_length=10),
        ),
    ]