from django import utils
import django
from django.db import models
from django.db.models.deletion import CASCADE
from datetime import timedelta
from django.db.models.fields import CharField, DurationField
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
        (timedelta(days=1), 'One day'),
        (timedelta(days=3), 'Three days'),
        (timedelta(weeks=1), 'One week'),
        (timedelta(weeks=2), 'Two weeks'),
        (timedelta(weeks=4), 'One month')])
    "TODO: If deadline:"
    reminder = models.CharField(blank=True, null=True, max_length=20, choices = [
        (timedelta(weeks=-1), 'Week before'),
        (timedelta(days=-2), '2 days before'),
        (timedelta(days=-1), '1 day before'),
        (timedelta(hours=-3), '3 hours before'),
        (timedelta(hours=-1), '1 hour before'),
        (timedelta(minutes=-30), '30 minutes before'),
        (timedelta(minutes=-30), '15 minutes before')])

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
    reminder = models.DurationField(default=timedelta(weeks=-4), choices = [
        (timedelta(weeks=-4), 'Month before'),
        (timedelta(weeks=-2), '2 weeks before'),
        (timedelta(weeks=-1), '1 week before'),
        (timedelta(days=-3), '3 days before'),
        (timedelta(days=-1), '1 day before'),
        (timedelta(hours=-3), '3 hours before'),
        (timedelta(hours=-1), '1 hour before')])

    @property
    def end_date(self):
        return self.start_date + self.duration

    def __str__(self):
        return "Event(name={}, repeatable={})".format(self.name, self.repeatable)

class Notification(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(default=None, max_length=30)
    'task_deadline_reminder = Task.deadline - Task.reminder'
    'task_postponed_reminder = timezone.now() + Task.postponed'
    'event_repeatable_reminder = timezone.now()'
    'event_start_reminder = timezone.now() - Event.reminder'
