from django.shortcuts import render, redirect
from .forms import PhotoUploadForm
from django.http import HttpResponse
from django.views.generic import TemplateView
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import FormView
from gallery.models import Image
from django.urls import reverse

# Create your views here.
class PhotoCreate(LoginRequiredMixin,FormView):
	login_url = '/login/'
	form_class = PhotoUploadForm
	template_name = 'photoUpload/photoUpload_form.html'

	def form_valid(self, form):


		image_data = form.files.getlist('data')

		for data in image_data:

			image = Image.objects.create(data=data)

			#image.image_albums.add(form.data['apk'])

			messages.success(self.request, "Images added successfully")

		return super().form_valid(form)



	def get_success_url(self):

		next_url = self.request.POST.get('next')

		return_url = reverse('gallery:image_list')

		if next_url:

			return_url = next_url

		return return_url

	def form_invalid(self, form):

		response = super().form_invalid(form)

		next_url = self.request.POST.get('next')

		if next_url:

            # TODO: Preserve error message

			return redirect(next_url)

		else:

			return response
