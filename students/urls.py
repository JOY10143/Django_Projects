from django.urls import path
from . import views

# Define the url path
urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'), # This is the about page
    path('contact/', views.contact, name='contact'), # This is the contact page
    path('courses/', views.courses, name='courses'),
    path('services/', views.services, name='services'),
]
