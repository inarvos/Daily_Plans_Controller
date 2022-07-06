from django.contrib import admin
from .models import Task, Event, Reminder, Notification

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    fields = ('name', 'description', 'parent', 'deadline', 'postponed', 'deadline_reminder', 'postponed_reminder', 'done')
    list_display = ['parent', 'id', 'name', 'description', 'deadline', 'postponed', 'deadline_reminder', 'postponed_reminder', 'done']

@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    fields = ('name', 'repeatable', 'description', 'start', 'duration', 'reminder') 
    list_display = ['id', 'name', 'repeatable', 'description', 'start', 'duration', 'reminder', 'end']

@admin.register(Reminder)
class ReminderAdmin(admin.ModelAdmin):
    fields = ('name', 'repeatable', 'description', 'start') 
    list_display = ['id', 'name', 'repeatable', 'description', 'start']
