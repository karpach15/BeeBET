# Generated by Django 2.2.7 on 2020-01-15 12:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account_profile', '0022_auto_20200115_1316'),
    ]

    operations = [
        migrations.RenameField(
            model_name='account_profile',
            old_name='driving_licens',
            new_name='driving_license',
        ),
    ]
