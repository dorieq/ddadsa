# Generated by Django 2.2.17 on 2023-03-26 10:25

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mo', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='posylka',
            name='cityArrival',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AddField(
            model_name='posylka',
            name='cityDestination',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AddField(
            model_name='posylka',
            name='cost',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=25),
        ),
        migrations.AddField(
            model_name='posylka',
            name='date',
            field=models.DateField(default=datetime.date.today),
        ),
        migrations.AddField(
            model_name='posylka',
            name='weight',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=25),
        ),
    ]
