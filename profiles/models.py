from django.contrib.auth.models import User
from django.db import models
from annoying.decorators import signals
import urllib, hashlib

""" Make changes to the user model so we can do email based users """
User._meta.get_field_by_name('username')[0].max_length = 150

""" Make the email field unique and indexed """
User._meta.get_field_by_name('email')[0].blank = False
# User._meta.get_field('email')[0].db_index = True


""" User Profiles to store additional information """
class UserProfile(models.Model):
  user = models.ForeignKey(User, unique=True, db_index=True)
  company = models.CharField(max_length=100, blank=True, null=True)
  twitter = models.CharField('Twitter Username', max_length=20, blank=True, null=True)
  facebook = models.CharField('Facebook URL', max_length=255, blank=True, null=True)
  linkedin = models.CharField('LinkedIn URL', max_length=255, blank=True, null=True)
  biography = models.TextField(blank=True, null=True)

  def __unicode__(self):
    return u'%s' % self.user

  def gravatar(self):
    return 'http://www.gravatar.com/avatar/%s?s=48' % hashlib.md5(self.email.lower()).hexdigest()

@signals.post_save(sender=User)
def create_profile(sender, instance, created, *args, **kwargs):
  if created == True:
    UserProfile(user=instance).save()
