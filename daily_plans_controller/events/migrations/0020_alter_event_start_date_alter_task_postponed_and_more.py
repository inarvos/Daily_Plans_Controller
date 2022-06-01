# Generated by Django 4.0.4 on 2022-05-31 23:58

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0019_alter_event_start_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='start_date',
            field=models.DateTimeField(default=datetime.datetime(2022, 5, 31, 23, 58, 7, 956659, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='task',
            name='postponed',
            field=models.CharField(blank=True, choices=[('1day', 'One day'), ('3days', 'Three days'), ('1week', 'One week'), ('2weeks', 'Two weeks'), ('1month', 'One month')], default=False, max_length=20),
        ),
        migrations.AlterField(
            model_name='task',
            name='reminder',
            field=models.CharField(blank=True, choices=[('week_before', 'Week before'), ('2days_before', '2 days before'), ('1day_before', '1 day before'), ('3hours_before', '3 hours before'), ('1hour_before', '1 hour before'), ('30min_before', '30 minutes before'), ('15min_before', '15 minutes before')], default=False, max_length=20),
        ),
    ]