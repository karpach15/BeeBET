# Generated by Django 2.2.7 on 2020-01-15 14:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account_profile', '0024_remove_account_profile_login'),
    ]

    operations = [
        migrations.AddField(
            model_name='account_profile',
            name='login',
            field=models.CharField(default=0, max_length=100),
            preserve_default=False,
        ),
    ]