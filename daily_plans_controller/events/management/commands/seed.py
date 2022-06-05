import random
from events.models import Event, Task
from django.core.management.base import BaseCommand
from faker import Faker
import datetime
from datetime import timedelta

faker = Faker()

def fill_events(count: int):
    for _ in range(count):
        name = faker.sentence()
        description = faker.text()
        repeatable = random.choice(('not_repeatable', 'once', 'daily', 'weekly', 'monthly', 'yearly'))
        start_date = faker.date_time_between(datetime.datetime.now() - timedelta(weeks=2), datetime.datetime.now() + timedelta(weeks=2))
        duration = timedelta(hours=random.choice((1, 3, 5, 10)))
        reminder = random.choice(('month_before', '2weeks_before', '1week_before', '3days_before', '1day_before', '3hours_before'))
        event = Event(name=name, description=description, repeatable=repeatable, start_date=start_date, duration=duration, reminder=reminder)
        event.save()
        
def fill_tasks(count: int):
    for _ in range(count):
        name = faker.sentence()
        description = faker.text()
        parent = random.choice(Task.objects.all()) if Task.objects.all() else None
        deadline = faker.date_time_between(datetime.datetime.now(), datetime.datetime.now() + timedelta(weeks=4))
        done = random.choice([True, False])
        done_at = datetime.datetime.now() if done else None
        archived = random.choice([True, False]) if done else False
        postponed = None if done else random.choice(('1day','3days','1week', '2weeks','1month'))
        reminder = None if done else random.choice(('month_before','2weeks_before','1week_before','3days_before','1day_before','3hours_before'))
        task = Task(name=name, description=description, parent=parent, deadline=deadline, done=done, done_at=done_at, archived=archived, postponed=postponed, reminder=reminder)
        task.save()

class Command(BaseCommand):
    help = 'Fill Event and Task models with Fake Data.'

    def add_arguments(self, parser):
        parser.add_argument('--fill-events', action='store_true', help = 'Fill Events with Fake Data.')
        parser.add_argument('--fill-tasks', action='store_true', help = 'Fill Tasks with Fake Data.')
        parser.add_argument('--clean-events', action='store_true', help = 'Clean Events from Fake Data.')
        parser.add_argument('--clean-tasks', action='store_true', help = 'Clean Tasks from Fake Data.')
        parser.add_argument('--count', type=int, default=50, help='Enter fill data count.')

    def handle(self, *args, **options):
        if options['fill_events']:
            fill_events(options['count'])
        if options['fill_tasks']:
            fill_tasks(options['count'])
        if options['clean_events']:
            for event in Event.objects.all():
                event.delete()
        if options['clean_tasks']:
            for task in Task.objects.all():
                task.delete()