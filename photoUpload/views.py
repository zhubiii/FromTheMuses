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
	success_url = '/'

	def form_valid(self, form):


                image_data = form.files.get('data')
                image_title = form.cleaned_data['title']
                image_date = form.cleaned_data['date']
                image_culture = form.cleaned_data['culture']
                image_period_prefix = form.cleaned_data['period_prefix']
                image_period = form.cleaned_data['period']
                image_object_type = form.cleaned_data['object_type']
                image_vase_technique = form.cleaned_data['vase_technique']
                image_vase_shape = form.cleaned_data['vase_shape']
                image_material = form.cleaned_data['material']
                image_country = form.cleaned_data['country']
                image_artist_or_attribution = form.cleaned_data['artist_or_attribution']
                image_associated_building = form.cleaned_data['associated_building']
                image_subject = form.cleaned_data['subject']
                image_description = form.cleaned_data['description']
                image_museum_collection = form.cleaned_data['museum_collection']

                image = Image.objects.create(
			data=image_data,
			title=image_title,
			date=image_date,
			culture=image_culture,
			period_prefix=image_period_prefix,
			period=image_period,
			object_type=image_object_type,
			vase_technique=image_vase_technique,
			vase_shape=image_vase_shape,
			material=image_material,
			country=image_country,
			artist_or_attribution=image_artist_or_attribution,
			associated_building=image_associated_building,
			subject=image_subject,
			description=image_description,
			museum_collection=image_museum_collection
			)

			#image.image_albums.add(form.data['apk'])

                messages.success(self.request, "Image has been successfully uploaded for review!")

                return super().form_valid(form)



#	def get_success_url(self):
#
#		next_url = self.request.POST.get('next')
#
#		return_url = reverse('gallery:image_list')
#
#		if next_url:
#
#			return_url = next_url
#
#		return return_url

	def form_invalid(self, form):

		response = super().form_invalid(form)

		next_url = self.request.POST.get('next')

		if next_url:

            # TODO: Preserve error message

			return redirect(next_url)

		else:

			return response
