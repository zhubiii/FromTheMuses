from django.urls import path

from .views import (
    HomePageView,
    AboutPageView,
    ContactPageView,
    ErrorPageView,
    LoggedOutPageView,
    MuseumsPageView,
    GlossaryPageView,
)

app_name = 'pages'
urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('home', HomePageView.as_view(), name='home'),
    path('about',AboutPageView.as_view(),name='about'),
    path('contact',ContactPageView.as_view(),name='contact'),
    path('error',ErrorPageView.as_view(),name='error'),
    path('goodbye',LoggedOutPageView.as_view(),name='goodbye'),
    path('museums',MuseumsPageView.as_view(),name='museums'),
    path('glossary',GlossaryPageView.as_view(),name='glossary'),
]