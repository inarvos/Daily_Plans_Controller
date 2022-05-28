from django.db import models
from django.utils import timezone

import datetime

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
    start_date = models.DateTimeField(default=timezone.now(), blank=False)
    duration = models.DurationField(default=datetime.timedelta(hours=1), blank=False)

    @property
    def end_date(self):
        return self.start_date + self.duration

    def __str__(self):
        return "Event(name={}, repeatable={})".format(self.name, self.repeatable)

class Task(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    parent = models.ForeignKey('self', blank=True, null=True, on_delete=models.CASCADE)
    deadline = models.DateTimeField(default=timezone.now(), blank=True)
    done = models.BooleanField(default=False)

    def save(self, *args, **kwargs):
        if self.done:
            children = Task.objects.filter(parent=self)
            for child in children:
                child.done = True
                child.save()
        super().save(*args, **kwargs)
    
    def __str__(self):
        return f"Task(name={self.name}, id={self.id})"
