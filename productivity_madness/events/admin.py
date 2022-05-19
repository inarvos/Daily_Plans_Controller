from django.contrib import admin
from .models import Event

@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    fields = ('name', 'repeatable') 
    list_display = ['id', 'name', 'repeatable']
