# Generated by Django 4.0.1 on 2022-01-22 22:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('day', '0005_remove_day_event'),
        ('event', '0006_remove_event_dates_affected'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='day',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='day.day'),
            preserve_default=False,
        ),
    ]
