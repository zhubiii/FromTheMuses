from django.urls import path
from .views import image_upload_form_view

app_name = 'imageUpload'
urlpatterns = [
    path('', image_upload_form_view, name='ImageUpload-form'),
]