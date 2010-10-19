from django import forms
from django.conf import settings
from django.core.mail import send_mail, BadHeaderError

class ContactForm(forms.Form):
  name = forms.CharField(max_length=50, widget=forms.TextInput(attrs={ 'size': '40' }))
  email = forms.EmailField(max_length=150, widget=forms.TextInput(attrs={ 'size': '40' }))
  subject = forms.CharField(max_length=100, widget=forms.TextInput(attrs={ 'size': '40' }))
  message = forms.CharField(widget=forms.Textarea(attrs={ 'cols': '80', 'rows': '10' }))

  def clean(self):
    cleaned_data = self.cleaned_data
    name = cleaned_data.get('name')
    email = cleaned_data.get('email')
    subject = cleaned_data.get('subject')
    message = cleaned_data.get('message')

    return cleaned_data

  def save(self):
    try:
      send_mail(self.cleaned_data.get('subject'), self.cleaned_data.get('message'), self.cleaned_data.get('email'), ['drewtemp@gmail.com'])
    except BadHeaderError:
      raise forms.ValidationError("Invalid header found.")

