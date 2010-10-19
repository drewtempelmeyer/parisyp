from django import template
from youngp.events.models import Event
from datetime import date

register = template.Library()

@register.inclusion_tag('events/event_items.html')
def events_for_month(month, year):
  month = int(month)
  year = int(year)
  greater_than_day = date(year, month, 1)

  if month == 12:
    year += 1
    month = 1
  else:
    month += 1

  less_than_day = date(year, month, 1)

  return { 'events': Event.objects.filter(occurring__gte=greater_than_day, occurring__lte=less_than_day) }


