from django.contrib.auth.models import User
from django.db import models
from autoslug.fields import AutoSlugField

# Create your models here.
"""
  Post model
  Blog post
"""
class Post(models.Model):
  title = models.CharField(max_length=125)
  slug = AutoSlugField(populate_from='title', unique=True, db_index=True)
  author = models.ForeignKey(User, db_index=True)
  tagline = models.CharField(max_length=150)
  body = models.TextField()
  publish_date = models.DateTimeField()
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)
  
  def __unicode__(self):
    return u'%s' % self.title

  @models.permalink
  def get_absolute_url(self):
    return ('post', [self.slug])

  class Meta:
    ordering = ['-publish_date']
