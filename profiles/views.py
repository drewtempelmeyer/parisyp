from django.contrib.auth import logout, authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.shortcuts import redirect
from annoying.decorators import render_to
from profiles.forms import ProfileForm, UserForm, UserCreateForm
from profiles.models import UserProfile

@render_to('registration/signup.html')
def signup(request):
  if request.method == 'POST':
    form = UserCreateForm(request.POST)
    if form.is_valid():
      form.save()
      messages.success(request, 'Your account was created successfully. You may now login using your email and password.')
      return redirect('/')
  else:
    form = UserCreateForm()
  return { 'form': form }

""" View for editing the current user's profile """
@login_required
@render_to('profiles/edit.html')
def edit(request):
  profile = UserProfile.objects.get(user=request.user)
  # Is this a POST method? If so, validate and save
  if request.method == 'POST':
    form = ProfileForm(request.POST, instance=profile)
    if form.is_valid():
      form.save()
      messages.success(request, 'Your profile was updated successfully.')
  else:
    form = ProfileForm(instance=profile)

  return { 'form': form }


""" View to logout current user """
def logout_view(request):
  logout(request)
  return redirect('/') 
