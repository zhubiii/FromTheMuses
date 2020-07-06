from django.urls import path
from .views import profile_check as profile_view

app_name = 'profiles'
urlpatterns = [
    path('<str:username>/', profile_view , name='User-Profile'),
]