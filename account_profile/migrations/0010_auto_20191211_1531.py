# Generated by Django 2.2.7 on 2019-12-11 13:31

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('account_profile', '0009_auto_20191211_1529'),
    ]

    operations = [
        migrations.RenameField(
            model_name='account_profile',
            old_name='status',
            new_name='account_status',
        ),
        migrations.AlterField(
            model_name='account_profile',
            name='account_create_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 12, 11, 13, 31, 2, 500380, tzinfo=utc)),
        ),
    ]