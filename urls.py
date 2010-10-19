from django.conf.urls.defaults import *

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'blog.views.index', {}, name='home'),
    (r'^profiles/', include('profiles.urls')),
    (r'^events/', include('events.urls')),
    (r'^news/', include('blog.urls')),
    url(r'^accounts/signup/$', 'profiles.views.signup', {}, name='signup'),
    (r'^accounts/login/$', 'django.contrib.auth.views.login'),
    (r'^contact/', include('contact.urls')),
    (r'^admin/', include(admin.site.urls)),
    url(r'^about/$', 'django.views.generic.simple.direct_to_template', { 'template': 'static/about.html' }, name='about'),
)
