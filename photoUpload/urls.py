from django.urls import path
from .views import PhotoCreate

app_name = 'photoUpload'
urlpatterns = [
    path('', PhotoCreate.as_view(), name='PhotoUpload-form'),
]
