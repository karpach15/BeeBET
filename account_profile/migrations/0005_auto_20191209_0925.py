# Generated by Django 3.0 on 2019-12-09 07:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account_profile', '0004_auto_20191209_0011'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account_profile',
            name='account_pic',
            field=models.CharField(default='https://icon-library.net/images/profile-icon-white/profile-icon-white-3.jpg', max_length=250),
        ),
    ]