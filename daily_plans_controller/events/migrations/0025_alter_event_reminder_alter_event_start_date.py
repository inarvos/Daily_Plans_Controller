# Generated by Django 4.0.4 on 2022-06-05 19:03

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0024_merge_20220605_1559'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='reminder',
            field=models.CharField(choices=[('month_before', 'Month before'), ('2weeks_before', '2 weeks before'), ('1week_before', '1 week before'), ('3days_before', '3 days before'), ('1day_before', '1 day before'), ('3hours_before', '3 hours before')], default='month_before', max_length=20),
        ),
        migrations.AlterField(
            model_name='event',
            name='start_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
