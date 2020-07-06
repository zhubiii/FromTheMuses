from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import TemplateView
from django.contrib import messages
from register.forms import UserUpdateForm,ProfileUpdateForm
from .models import Profile
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

# Create your views here.
def profile_check(request, username, *args, **kwargs):
    if request.user.is_anonymous:
        messages.warning(request, 'Please login or register to view profiles',extra_tags='danger')
    return profile(request, username, *args, **kwargs)

@login_required(login_url='/login')
def profile(request, username, *args, **kwargs):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)

        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            uname = request.user.username
            messages.success(request,f'Your profile has been updated!',extra_tags='success')
            return redirect("/profiles/"+uname)

    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

    obj = get_object_or_404(User, username=username)
    context = {
        'u_form': u_form,
        'p_form': p_form,
        'object': obj
    }

    return render(request, 'profiles/profile.html', context)