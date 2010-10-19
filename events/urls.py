from django.conf.urls.defaults import *
from django.views.generic import list_detail
from events.models import Event

event_list_info = {
  'queryset': Event.objects.all(),
  'template_object_name': 'event',
}

urlpatterns = patterns('',
  #url(r'^$', list_detail.object_list, dict(event_list_info, paginate_by=20), name='events'),
  url(r'^$', 'events.views.index', {}, name='events'),
  url(r'^(?P<slug>[\w-]+)/$', list_detail.object_detail, event_list_info, name='event'),
  url(r'^(?P<slug>[\w-]+)/attending/$', 'events.views.attending', {}, name='attending_event'),
  url(r'^(?P<slug>[\w-]+)/not-attending/$', 'events.views.unattend', {}, name='unattend_event'),
)
