# Generated by Django 2.2.7 on 2020-01-26 18:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('drivers', '0014_drivers_coeficient'),
    ]

    operations = [
        migrations.AddField(
            model_name='drivers',
            name='custom_coeficient',
            field=models.FloatField(default=0),
        ),
    ]