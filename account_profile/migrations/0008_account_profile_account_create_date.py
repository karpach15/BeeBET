# Generated by Django 2.2.7 on 2019-12-11 13:28

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('account_profile', '0007_account_profile_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='account_profile',
            name='account_create_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 12, 11, 13, 28, 35, 534571, tzinfo=utc)),
            preserve_default=False,
        ),
    ]
