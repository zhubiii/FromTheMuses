from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView
from django.contrib.messages.views import SuccessMessageMixin

# Create your views here.
class HomePageView(TemplateView):
    template_name = 'pages/home.html'

class AboutPageView(TemplateView):
    template_name = 'pages/about.html'

class ContactPageView(TemplateView):
    template_name = 'pages/contact.html'

class ErrorPageView(TemplateView):
    template_name = 'pages/error.html'

class LoggedOutPageView(SuccessMessageMixin, TemplateView):
    success_message = 'You have successfully logged out!'
    template_name = 'pages/logged_out.html'

class MuseumsPageView(TemplateView):
    template_name = 'pages/museums.html'

class GlossaryPageView(TemplateView):
    template_name = 'pages/glossary.html'
