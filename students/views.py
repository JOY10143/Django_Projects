from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
# A function to return a message
def home(request):
    return HttpResponse("Welcome to Denory Academy! This is homepage of our students app.")

def about(request):
    return HttpResponse("Welcome to the About page. Learn more about Denory Academy.")

def contact(request):
    return HttpResponse("Welcome to the Contact page. Reach for more information.")

def courses(request):
    return HttpResponse("Wlcome to the Courses page. Explore our available courses.")

def services(request):
    return HttpResponse("Welcome to the Services page. Discover the services we offer.")
