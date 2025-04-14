
from django.urls import path
from . import views

urlpatterns = [
   path('hello/', views.say_hello, name='say_hello'), 
   path('home/', views.HomePage, name='home'),
   path('about/', views.AboutPage, name='about'),
   path('contact/', views.ContactPage, name='contact'),
   path('services/', views.ServicesPage, name='services'),
]
