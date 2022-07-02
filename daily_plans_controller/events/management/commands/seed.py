import random
from events.models import Event, Task, Reminder
from django.core.management.base import BaseCommand
from faker import Faker
import datetime
from datetime import timedelta

faker = Faker()
        
#TODO: Fix 'None if done' which is not working.
def fill_tasks(count: int):
    for _ in range(count):
        name = faker.sentence()
        description = faker.text()
        parent = random.choice(Task.objects.all()) if Task.objects.all() else None
        done = random.choice([True, False])
        deadline = None if done else faker.date_time_between(datetime.datetime.now(), datetime.datetime.now() + timedelta(weeks=4))
        done_at = datetime.datetime.now() if done else None
        archived = random.choice([True, False]) if done else False
        postponed = None if done else random.choice((timedelta(), timedelta(days=1), timedelta(days=3), timedelta(weeks=1), timedelta(weeks=2), timedelta(weeks=4)))
        deadline_reminder = None if done else random.choice((timedelta(), timedelta(weeks=-1), timedelta(days=-2), timedelta(days=-1), timedelta(hours=-3), timedelta(hours=-1)))
        postponed_reminder = None if done else random.choice((timedelta(), timedelta(weeks=-1), timedelta(days=-2), timedelta(days=-1), timedelta(hours=-3), timedelta(hours=-1)))
        task = Task(name=name, description=description, parent=parent, deadline=deadline, postponed=postponed, deadline_reminder=deadline_reminder, postponed_reminder=postponed_reminder, done=done, done_at=done_at, archived=archived)
        task.save()

def fill_events(count: int):
    for _ in range(count):
        name = faker.sentence()
        description = faker.text()
        repeatable = random.choice((timedelta(days=1), timedelta(weeks=1), timedelta(weeks=4), timedelta(days=365)))
        start = faker.date_time_between(datetime.datetime.now() - timedelta(weeks=2), datetime.datetime.now() + timedelta(weeks=2))
        duration = timedelta(hours=random.choice(range(24)))
        reminder = random.choice((timedelta(weeks=-4), timedelta(weeks=-2), timedelta(weeks=-1), timedelta(days=-3), timedelta(days=-1), timedelta(hours=-3), timedelta(hours=-1)))
        event = Event(name=name, description=description, repeatable=repeatable, start=start, duration=duration, reminder=reminder)
        event.save()

def fill_reminders(count: int):
    for _ in range(count):
        name = faker.sentence()
        description = faker.text()
        repeatable = random.choice((timedelta(days=1), timedelta(weeks=1), timedelta(weeks=4), timedelta(days=365)))
        start = faker.date_time_between(datetime.datetime.now() - timedelta(weeks=2), datetime.datetime.now() + timedelta(weeks=2))
        reminder = Reminder(name=name, description=description, repeatable=repeatable, start=start)
        reminder.save()

class Command(BaseCommand):
    help = 'Fill Task, Event and Reminder models with Fake Data.'

    def add_arguments(self, parser):
        parser.add_argument('--fill-tasks', action='store_true', help = 'Fill Tasks with Fake Data.')
        parser.add_argument('--fill-events', action='store_true', help = 'Fill Events with Fake Data.')
        parser.add_argument('--fill-reminders', action='store_true', help = 'Fill Reminders with Fake Data.')
        parser.add_argument('--clean-tasks', action='store_true', help = 'Clean Tasks from Fake Data.')
        parser.add_argument('--clean-events', action='store_true', help = 'Clean Events from Fake Data.')
        parser.add_argument('--clean-reminders', action='store_true', help = 'Clean Reminders from Fake Data.')
        parser.add_argument('--count', type=int, default=50, help='Enter fill data count.')

    def handle(self, *args, **options):
        if options['fill_tasks']:
            fill_tasks(options['count'])
        if options['fill_events']:
            fill_events(options['count'])
        if options['fill_reminders']:
            fill_reminders(options['count'])
        if options['clean_tasks']:
            for task in Task.objects.all():
                task.delete()
        if options['clean_events']:
            for event in Event.objects.all():
                event.delete()
        if options['clean_reminders']:
            for reminder in Reminder.objects.all():
                reminder.delete()
