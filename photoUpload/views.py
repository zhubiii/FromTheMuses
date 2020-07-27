from django.shortcuts import render, redirect
from .forms import ImageUploadForm
from django.http import HttpResponse
from django.views.generic import TemplateView
from django.contrib import message

# Create your views here.
def image_upload_form_view(response):
    if response.method == "POST":
        form = ImageUploadForm(response.POST)
        if form.is_valid():
            form.save()
            messages.success(response,f'Your image has successfully been uploaded for review!')
            return redirect("/")
    else:
        form = ImageUploadForm()
    return render(response,"photoUpload/photoUpload_form.html",{form:form})