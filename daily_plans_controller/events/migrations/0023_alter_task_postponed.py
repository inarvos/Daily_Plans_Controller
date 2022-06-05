# Generated by Django 4.0.4 on 2022-06-04 18:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0022_alter_event_start_date_alter_task_postponed_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='postponed',
            field=models.CharField(blank=True, choices=[('1day', 'One day'), ('3days', 'Three days'), ('1week', 'One week'), ('2weeks', 'Two weeks'), ('1month', 'One month')], max_length=20, null=True),
        ),
    ]