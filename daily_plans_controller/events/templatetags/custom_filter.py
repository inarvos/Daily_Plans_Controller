from django import template

register = template.Library()

@register.filter(name='custom_date')
def custom_date(value, args):
  return value.strftime(args)
