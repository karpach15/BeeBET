# Generated by Django 2.2.7 on 2020-01-15 11:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account_profile', '0019_account_profile_email'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='account_profile',
            name='date_of_getting_driving_licens',
        ),
    ]