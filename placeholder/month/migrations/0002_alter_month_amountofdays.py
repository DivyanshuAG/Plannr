# Generated by Django 4.0.1 on 2022-01-22 07:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('month', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='month',
            name='amountOfDays',
            field=models.IntegerField(),
        ),
    ]