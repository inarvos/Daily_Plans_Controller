from django import utils
import django
from django.db import models
from django.db.models.deletion import CASCADE
from django.db.models.fields import CharField
import django.utils.timezone as timezone
import datetime

class Task(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    parent = models.ForeignKey('self', blank=True, null=True, on_delete=CASCADE)
    deadline = models.DateTimeField(blank=True, null=True)
    done = models.BooleanField(default=False)
    "TODO If done -> archive"
    done_at = models.DateTimeField(null=True)
    archived = models.BooleanField(default=False)
    "TODO"
    postponed = models.CharField(blank=True, null=True, max_length=20, choices = [
        ('1day', 'One day'),
        ('3days', 'Three days'),
        ('1week', 'One week'),
        ('2weeks', 'Two weeks'),
        ('1month', 'One month')])
    "TODO: If deadline:"
    reminder = models.CharField(blank=True, null=True, max_length=20, choices = [
        ('week_before', 'Week before'),
        ('2days_before', '2 days before'),
        ('1day_before', '1 day before'),
        ('3hours_before', '3 hours before'),
        ('1hour_before', '1 hour before'),
        ('30min_before', '30 minutes before'),
        ('15min_before', '15 minutes before')])

    """
    TODO
    Notifications:
        if deadline + reminder: create Notification = deadline - reminder;
        if postponed: create Notification = Today + postpone time
    """

    def save(self, *args, **kwargs):
        if self.done:
            children = Task.objects.filter(parent=self)
            for child in children:
                child.done = True
                child.save()
            self.done_at = timezone.now()
        elif not self.done and self.done_at:
            self.done_at = None
        super().save(*args, **kwargs)
    
    def __str__(self):
        return f"Task(name={self.name}, id={self.id})"

class Event(models.Model):
    name = models.CharField(max_length=50)
    repeatable = models.CharField(max_length=20, choices = [
        ('not_repeatable', 'Not repeatable'),
        ('once', 'Once'),
        ('daily', 'Daily'),
        ('weekly', 'Weekly'),
        ('monthly', 'Monthly'),
        ('yearly', 'Yearly')])
    description = models.TextField(max_length=200, blank=True)
    start_date = models.DateTimeField(default=timezone.now, blank=False)
    duration = models.DurationField(default=datetime.timedelta(hours=1), blank=False)
    "TODO"
    reminder = CharField(default='month_before', max_length=20, choices = [
        ('month_before', 'Month before'),
        ('2weeks_before', '2 weeks before'),
        ('1week_before', '1 week before'),
        ('3days_before', '3 days before'),
        ('1day_before', '1 day before'),
        ('3hours_before', '3 hours before')])

    "TODO Notification = start_date - reminder"

    @property
    def end_date(self):
        return self.start_date + self.duration

    def __str__(self):
        return "Event(name={}, repeatable={})".format(self.name, self.repeatable)

"TODO"
class Notification(models.Model):
    name = models.CharField(max_length=50)
    'task_deadline_reminder = Task.deadline - Task.reminder'
    'task_postponed_reminder = timezone.now() + Task.postponed'
    'event_repeatable_reminder = timezone.now()'
    'event_start_reminder = timezone.now() - Event.reminder'
