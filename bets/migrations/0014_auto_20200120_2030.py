# Generated by Django 2.2.7 on 2020-01-20 18:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bets', '0013_stake_bet_date'),
    ]

    operations = [
        migrations.RenameField(
            model_name='stake',
            old_name='paymnet_method',
            new_name='payment_method',
        ),
    ]
