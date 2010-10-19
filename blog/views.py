from blog.models import Post
from events.models import Event
from annoying.decorators import render_to
import datetime

@render_to('index.html')
def index(request):
  events = Event.objects.filter(occurring__gte=datetime.datetime.now())[:5]
  posts = Post.objects.filter(publish_date__lte=datetime.datetime.now())[:5]
  return { 'events': events, 'posts': posts }
