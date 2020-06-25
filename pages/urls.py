from django.urls import path

from .views import (
    HomePageView,
    AboutPageView,
    ContactPageView,
    ErrorPageView
)

app_name = 'pages'
urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('about',AboutPageView.as_view(),name='about'),
    path('contact',ContactPageView.as_view(),name='contact'),
    path('error',ErrorPageView.as_view(),name='error')
]