from django.db import models

class Event(models.Model):
    name = models.CharField(max_length=50)
    repeatable = models.CharField(max_length=20, choices = [
        ('not_repeatable', 'Not repeatable'),
        ('once', 'Once'),
        ('daily', 'Daily'),
        ('weekly', 'Weekly'),
        ('monthly', 'Monthly'),
        ('yearly', 'Yearly')])

    def __str__(self):
        return "Event(name={}, repeatable={})".format(self.name, self.repeatable)
