from django.urls import path
from .views import register_form_view,RegisterSuccessPageView

app_name = 'register'
urlpatterns = [
    path('', register_form_view, name='register-form'),
    path('registration-successful', RegisterSuccessPageView.as_view(), name='registration-success')

]