# Generated by Django 2.2.7 on 2020-01-15 14:52

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('drivers', '0012_auto_20200115_1652'),
    ]

    operations = [
        migrations.AddField(
            model_name='drivers',
            name='reg_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
