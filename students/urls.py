from django.urls import path
from . import views

# Define the url path
urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('courses/', views.courses, name='courses'),
    path('services/', views.services, name='services'),
]
