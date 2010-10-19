from django.conf.urls.defaults import *
from django.views.generic import list_detail
from blog.models import Post
import datetime

blog_list_info = {
  'queryset': Post.objects.filter(publish_date__lte=datetime.datetime.now()),
  'template_object_name': 'post',
}

urlpatterns = patterns('',
  url(r'^$', list_detail.object_list, dict(blog_list_info, paginate_by=10), name='blog'),
  url(r'^(?P<slug>[\w-]+)/$', list_detail.object_detail, blog_list_info, name='post')
)
