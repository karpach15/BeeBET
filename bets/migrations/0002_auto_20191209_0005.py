# Generated by Django 3.0 on 2019-12-08 22:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bets', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='stakes',
            name='surname',
        ),
        migrations.AlterField(
            model_name='stakes',
            name='name',
            field=models.CharField(choices=[('Marko', 'Marko Karpats')], max_length=50),
        ),
    ]