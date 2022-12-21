from django import template

register = template.Library()

@register.filter(name='custom_date')
def custom_date(value, args):
    return value.strftime(args)

@register.filter(name='custom_practice')
def custom_practice(value, args):
    return value 
