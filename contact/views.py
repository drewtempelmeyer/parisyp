from django.conf import settings
from django.shortcuts import render_to_response, redirect
from django.template import RequestContext
from contact.forms import ContactForm
from contact.akismet import Akismet

def index(request):
  if request.method == 'POST':
    form = ContactForm(request.POST)
    if form.is_valid():
      akis = Akismet(key=settings.AKISMET_KEY)
      data = { 'user_ip': request.META['REMOTE_ADDR'], 'user_agent': request.META['HTTP_USER_AGENT'] }
      if akis.comment_check(comment=form.cleaned_data.get('message'), data=data) == False:
        form.save()
        return redirect('contact_thanks')
  else:
    form = ContactForm()

  return render_to_response('contact/index.html', { 'form': form }, context_instance=RequestContext(request))

