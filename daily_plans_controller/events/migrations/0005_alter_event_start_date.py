# Generated by Django 4.0.4 on 2022-05-22 17:02

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0004_alter_event_start_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='start_date',
            field=models.DateTimeField(default=datetime.datetime(2022, 5, 22, 17, 2, 3, 71037, tzinfo=utc)),
        ),
    ]
