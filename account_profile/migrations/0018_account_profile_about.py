# Generated by Django 3.0 on 2020-01-14 19:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account_profile', '0017_auto_20200114_2112'),
    ]

    operations = [
        migrations.AddField(
            model_name='account_profile',
            name='about',
            field=models.TextField(blank=True),
        ),
    ]
