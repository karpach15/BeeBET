# Generated by Django 2.2.7 on 2020-01-15 19:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('races', '0008_auto_20191209_0925'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Future_Races',
        ),
        migrations.DeleteModel(
            name='Past_Races',
        ),
    ]
