# Generated by Django 2.2.7 on 2019-12-11 13:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account_profile', '0006_remove_account_profile_driving_licens'),
    ]

    operations = [
        migrations.AddField(
            model_name='account_profile',
            name='status',
            field=models.CharField(choices=[('True', 'True'), ('False', 'False')], default='False', max_length=10),
        ),
    ]
