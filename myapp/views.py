from django.shortcuts import render 
from django.http import HttpResponse


# Create your views here.
def say_hello(request):
    return HttpResponse("Hello, world!")
def HomePage(request):
    return render(request,'home.html')
def AboutPage(request):
    return render(request,'about.html')
def ContactPage(request):
    return render(request,'contact.html')
def ServicesPage(request):
    return render(request,'services.html')
