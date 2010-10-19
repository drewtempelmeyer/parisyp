from django.conf.urls.defaults import *

urlpatterns = patterns('',
  url(r'^$', 'contact.views.index', {}, name='contact'),
  url(r'^thanks/$', 'django.views.generic.simple.direct_to_template', { 'template': 'contact/thanks.html' }, name='contact_thanks'),
)
