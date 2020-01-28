# Generated by Django 2.2.7 on 2020-01-15 14:48

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('drivers', '0008_delete_drivers'),
    ]

    operations = [
        migrations.CreateModel(
            name='Drivers',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('login', models.CharField(max_length=30)),
                ('reg_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('status', models.CharField(choices=[('True', 'True'), ('False', 'False')], default='False', max_length=10)),
            ],
        ),
    ]
