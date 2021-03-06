from django.shortcuts import render, redirect
from .forms import RegisterForm
from django.http import HttpResponse
from django.views.generic import TemplateView
from django.contrib.auth import authenticate, login
from django.contrib import messages

# Create your views here.
def register_form_view (response):
    if response.method == "POST":
        form = RegisterForm(response.POST)
        if form.is_valid():
            form.save()
            new_user = authenticate(username=form.cleaned_data['username'],password=form.cleaned_data['password1'],)
            login(response,new_user)
            messages.success(response,f'You have successfully registered!')
            return redirect("/")
    else:
        form = RegisterForm()
    return render(response,"register/register_form.html",{"form":form})
