# Generated by Django 4.0.1 on 2022-01-22 09:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('day', '0002_day_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='day',
            name='week',
        ),
    ]
