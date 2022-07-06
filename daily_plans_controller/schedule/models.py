from datetime import timedelta
from django import utils
import django
from django.db import models
from django.db.models.deletion import CASCADE
import django.utils.timezone as timezone
import datetime

class Task(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=100, blank=True)
    parent = models.ForeignKey('self', blank=True, null=True, on_delete=CASCADE)
    deadline = models.DateTimeField(blank=True, null=True)
    done = models.BooleanField(default=False)
    done_at = models.DateTimeField(null=True)
    archived = models.BooleanField(default=False)
    postponed = models.DurationField(blank=True, null=True, choices = [
        (timedelta(days=1), 'One day'),
        (timedelta(days=3), 'Three days'),
        (timedelta(weeks=1), 'One week'),
        (timedelta(weeks=2), 'Two weeks'),
        (timedelta(weeks=4), 'One month')])
    deadline_reminder = models.DurationField(blank=True, null=True, choices = [
        (timedelta(weeks=-1), 'Week before'),
        (timedelta(days=-2), '2 days before'),
        (timedelta(days=-1), '1 day before'),
        (timedelta(hours=-3), '3 hours before'),
        (timedelta(hours=-1), '1 hour before')])
    postponed_reminder = models.DurationField(blank=True, null=True, choices = [
        (timedelta(weeks=-1), 'Week before'),
        (timedelta(days=-2), '2 days before'),
        (timedelta(days=-1), '1 day before'),
        (timedelta(hours=-3), '3 hours before'),
        (timedelta(hours=-1), '1 hour before')])

    def save(self, *args, **kwargs):
        if self.done:
            children = Task.objects.filter(parent=self)
            for child in children:
                child.done = True
                child.save()
            self.done_at = timezone.now()
            self.archived = True
            self.deadline = None
            self.postponed = None
            self.deadline_reminder = None
            self.postponed_reminder = None
        elif not self.done and self.done_at:
            self.done_at = None
            self.archived = False
        super().save(*args, **kwargs)
    
    def __str__(self):
        return f"Task(name={self.name}, id={self.id})"

class Event(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=200, blank=True)
    repeatable = models.DurationField(default=timedelta(weeks=4), choices = [
        (timedelta(days=1), 'Daily'),
        (timedelta(weeks=1), 'Weekly'),
        (timedelta(weeks=4), 'Monthly'),
        (timedelta(days=365), 'Yearly')])
    start = models.DateTimeField(default=timezone.now, blank=False)
    duration = models.DurationField(default=timedelta(hours=1), blank=False, choices = [
        (timedelta(hours=2), 'Two hours'),
        (timedelta(hours=3), 'Three hours'),
        (timedelta(hours=6), 'Six hours'),
        (timedelta(hours=12), 'Twelve hours'),
        (timedelta(days=1), 'One day')])
    reminder = models.DurationField(default=timedelta(weeks=-4), choices = [
        (timedelta(weeks=-4), 'Month before'),
        (timedelta(weeks=-2), '2 weeks before'),
        (timedelta(weeks=-1), '1 week before'),
        (timedelta(days=-3), '3 days before'),
        (timedelta(days=-1), '1 day before'),
        (timedelta(hours=-3), '3 hours before'),
        (timedelta(hours=-1), '1 hour before')])

    @property
    def end(self):
        return self.start + self.duration

    def __str__(self):
        return "Event(name={}, repeatable={})".format(self.name, self.repeatable)

class Reminder(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=200, blank=True)
    repeatable = models.DurationField(default=timedelta(weeks=4), choices = [
        (timedelta(days=1), 'Daily'),
        (timedelta(weeks=1), 'Weekly'),
        (timedelta(weeks=4), 'Monthly'),
        (timedelta(days=365), 'Yearly')])
    start = models.DateTimeField(default=timezone.now, blank=False)

    def __str__(self):
        return "Reminder(name={}, repeatable={})".format(self.name, self.repeatable)

class Notification(models.Model):
    """task_deadline_reminder = Task.deadline - Task.reminder
    task_postponed_reminder = timezone.now() + Task.postponed
    event_repeatable_reminder = timezone.now()
    event_start_reminder = timezone.now() - Event.reminder"""
