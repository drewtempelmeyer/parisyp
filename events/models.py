from django.contrib.auth.models import User
from django.db import models
import datetime

class Event(models.Model):
  title = models.CharField(max_length=100)
  slug = models.SlugField(max_length=100, blank=True)
  occurring = models.DateTimeField()
  require_invitation = models.BooleanField(blank=True, default=False)
  venue = models.CharField(max_length=65, blank=True)
  address = models.TextField(blank=True)
  description = models.TextField()
  created_by = models.ForeignKey(User, related_name='created_events', db_index=True)
  created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)
  updated_at = models.DateTimeField(auto_now=True, blank=True)
  attending = models.ManyToManyField(User, related_name='attending', blank=True)
  maybe_attending = models.ManyToManyField(User, related_name='maybe_attending', blank=True)
  not_attending = models.ManyToManyField(User, related_name='not_attending', blank=True)

  def __unicode__(self):
    return u'%s' % self.title

  @models.permalink
  def get_absolute_url(self):
    return ('event', [self.slug])

  def is_attending(self, user):
    user_count = self.attending.filter(user=user).count()
    if user_count == 0:
      return False
    else:
      return True


  class Meta:
    ordering = ['occurring']
