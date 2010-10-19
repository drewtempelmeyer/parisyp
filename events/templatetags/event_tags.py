from django.contrib.auth.models import User
from django import template
from django.template.defaultfilters import stringfilter
from annoying.functions import get_object_or_None
from youngp.events.models import Event
import hashlib

register = template.Library()

"""
  GRAVATARZ
"""
@register.filter
@stringfilter
def md5(value):
  """ Replace value with gravatar URL for specified email address """
  return hashlib.md5(value).hexdigest()


""" This node will actually perform all of the work for us """
class UserAttendingNode(template.Node):
  def __init__(self, event, user):
    self.event = template.Variable(event)
    self.user = template.Variable(user)

  def render(self, context):
    event = self.event.resolve(context)
    user = self.user.resolve(context)

    if event.attending.filter(pk=user.id).count() == 0:
      self.is_attending = False
    else:
      self.is_attending = True

    context['is_attending'] = self.is_attending
    return ''


@register.tag
def is_attending(parser, token):
  try:
    tag_name, event, user = token.contents.split(None)
  except ValueError:
    raise template.TemplateSyntaxError, "%r tag requires arguments" % token.contents.split(None)[0]

  return UserAttendingNode(event, user)
