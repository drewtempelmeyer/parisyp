from django.conf.urls.defaults import *
from django.contrib.auth.models import User
from django.views.generic import list_detail

user_list_info = {
  'queryset': User.objects.all(),
  'template_object_name': 'u',
}

urlpatterns = patterns('',
  url(r'^$', list_detail.object_list, dict(user_list_info, paginate_by = 15, template_name = 'profiles/index.html'), name='profiles'),
  url(r'^(?P<object_id>\d+)/$', list_detail.object_detail, dict(user_list_info, template_name = 'profiles/show.html'), name='profile'),
  url(r'^edit/$', 'profiles.views.edit', {}, name='edit_profile'),
  url(r'^logout/$', 'profiles.views.logout_view', {}, name='logout'),
)
