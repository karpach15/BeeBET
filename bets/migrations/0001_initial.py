# Generated by Django 2.2.7 on 2019-12-08 21:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Stakes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('surname', models.CharField(max_length=50)),
                ('stake', models.FloatField()),
                ('expected_winner_name', models.CharField(max_length=50)),
                ('expected_winner_surname', models.CharField(max_length=50)),
            ],
        ),
    ]
