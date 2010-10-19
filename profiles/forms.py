from django import forms
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _
from profiles.models import UserProfile

class UserForm(forms.ModelForm):
  class Meta:
    model = User

class ProfileForm(forms.ModelForm):
  class Meta:
    model = UserProfile
    exclude = ('user',)
    fields = ['first_name', 'last_name', 'company', 'email', 'twitter', 'facebook', 'linkedin', 'biography']

  first_name = forms.CharField(max_length=30, widget=forms.TextInput(attrs={ 'size': '30' }))
  last_name = forms.CharField(max_length=30, widget=forms.TextInput(attrs={ 'size': '30' }))
  company = forms.CharField(max_length=25, widget=forms.TextInput(attrs={ 'size': '25' }), required=False)
  email = forms.EmailField(max_length=150, widget=forms.TextInput(attrs={ 'size': '50' }))
  twitter = forms.CharField(max_length=25, widget=forms.TextInput(attrs={ 'size': '25' }), required=False)
  facebook = forms.CharField(max_length=120, widget=forms.TextInput(attrs={ 'size': '45' }), required=False)
  linkedin = forms.CharField(max_length=120, widget=forms.TextInput(attrs={ 'size': '45' }), required=False)
  biography = forms.CharField(widget=forms.Textarea(attrs={ 'cols': '80', 'rows': '9' }), required=False)

  def __init__(self, *args, **kwargs):
    super(ProfileForm, self).__init__(*args, **kwargs)
    self.fields['first_name'].initial = self.instance.user.first_name
    self.fields['last_name'].initial = self.instance.user.last_name
    self.fields['email'].initial = self.instance.user.email

  def clean(self):
    cleaned_data = self.cleaned_data
    company = cleaned_data.get('company')
    twitter = cleaned_data.get('twitter')
    facebook = cleaned_data.get('facebook')
    linkedin = cleaned_data.get('linkedin')
    biography = cleaned_data.get('biography')

    return cleaned_data

  def save(self, commit=True):
    profile = super(ProfileForm, self).save(commit=False)
    self.instance.user.username = self.cleaned_data.get('email')
    self.instance.user.first_name = self.cleaned_data.get('first_name')
    self.instance.user.last_name = self.cleaned_data.get('last_name')
    self.instance.user.email = self.cleaned_data.get('email')
    if commit:
      self.instance.user.save()
      profile.save()
    return profile


class UserCreateForm(forms.ModelForm):
  """
    Form that creates the user account
  """
  username = forms.EmailField(label=_("Email"), max_length=150,
    error_messages = { 'invalid': _("This must be a valid email address.") }, widget=forms.TextInput(attrs={ 'size': '40' }))
  password1 = forms.CharField(label=_("Password"), widget=forms.PasswordInput(attrs={ 'size': '40' }))
  password2 = forms.CharField(label=_("Password confirmation"), widget=forms.PasswordInput(attrs={ 'size': '40' }))
  first_name = forms.CharField(max_length=30, widget=forms.TextInput(attrs={ 'size': '40' }), required=True)
  last_name = forms.CharField(max_length=30, widget=forms.TextInput(attrs={ 'size': '40' }), required=True)

  class Meta:
    model = User
    fields = ('username', 'first_name', 'last_name')

  def clean_username(self):
    username = self.cleaned_data["username"]
    try:
      User.objects.get(username=username)
    except User.DoesNotExist:
      return username
    raise forms.ValidationError(_("A user with that email address already exists."))

  def clean_password2(self):
    password1 = self.cleaned_data.get("password1", "")
    password2 = self.cleaned_data["password2"]
    if password1 != password2:
      raise forms.ValidationError(_("The two password fields do not match."))
    return password2

  def save(self, commit=True):
    user = super(UserCreateForm, self).save(commit=False)
    user.set_password(self.cleaned_data["password1"])
    user.email = self.cleaned_data["username"]
    if commit:
      user.save()
    return user
