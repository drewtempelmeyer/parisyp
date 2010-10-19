from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404, redirect
from annoying.decorators import render_to
from events.models import Event

@render_to('events/index.html')
def index(request):
  event_dates = Event.objects.dates('occurring', 'month')
  return { 'event_dates': event_dates, 'Event': Event }

def attending(request, slug):
  if request.user.is_authenticated():
    event = get_object_or_404(Event, slug=slug)
    event.attending.add(request.user)

  return redirect('event', slug=slug)

def unattend(request, slug):
  if request.user.is_authenticated():
    event = get_object_or_404(Event, slug=slug)
    event.attending.remove(request.user)

  return redirect('event', slug=slug)
