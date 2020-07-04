from django.shortcuts import render, redirect
from .forms import RegisterForm
from django.http import HttpResponse
from django.views.generic import TemplateView

# Create your views here.
def register_form_view (response):
    if response.method == "POST":
        form = RegisterForm(response.POST)
        if form.is_valid():
            form.save()
            return redirect("/register/registration-successful")
    else:
        form = RegisterForm()
    return render(response,"register/register_form.html",{"form":form})

class RegisterSuccessPageView(TemplateView):
    template_name = 'register/register_success.html'