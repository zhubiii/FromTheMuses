from django.urls import path
from .views import register_form_view

app_name = 'register'
urlpatterns = [
    path('', register_form_view, name='register-form')
]