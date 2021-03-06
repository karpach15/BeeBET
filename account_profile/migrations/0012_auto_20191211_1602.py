# Generated by Django 2.2.7 on 2019-12-11 14:02

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('account_profile', '0011_auto_20191211_1542'),
    ]

    operations = [
        migrations.RenameField(
            model_name='account_profile',
            old_name='name',
            new_name='account_name',
        ),
        migrations.RenameField(
            model_name='account_profile',
            old_name='surname',
            new_name='account_surname',
        ),
        migrations.AlterField(
            model_name='account_profile',
            name='account_create_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 12, 11, 14, 2, 22, 210150, tzinfo=utc)),
        ),
    ]
