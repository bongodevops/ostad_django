from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def say_hello(request):
    return HttpResponse("Hello, world!")
def HomePage(request):
    return render(request,'home.html')
def AboutPage(request):
    return render(request,'about.html')
def ContactPage(request):
    
    profile =[
        "fb.com/hafizurrahmanomar/",
        "github.com/hafizurrahmanomar",
        "linkedin.com/in/hafizurrahmanomar",
        "instagram.com/hafizurrahmanomar/",
        "twitter.com/hafizurrahmanomar",
        "youtube.com/@hafizurrahmanomar",
        "tiktok.com/@hafizurrahmanomar",
        "pinterest.com/hafizurrahmanomar",
        "stackoverflow.com/users/20220623/hafizurrahmanomar",
        "dribbble.com/hafizurrahmanomar",
        "behance.net/hafizurrahmanomar",
        "medium.com/@hafizurrahmanomar",
        "dev.to/hafizurrahmanomar",
        "quora.com/profile/Hafizur-Rahman-Omar",
        "goodreads.com/hafizurrahmanomar",
        "blogger.com/hafizurrahmanomar",
        "medium.com/@hafizurrahmanomar",
    ]
    
    return render(request,'contact.html',{"social_links":profile,})
def ServicesPage(request):
    
    services = {
        "serve_01": "Web Development",
        "serve_02": "Web Design",
        "serve_03": "UI/UX Design",
        "serve_04": "Graphic Design",
        "serve_05": "SEO Optimization",
        "serve_06": "Digital Marketing",
        "serve_07": "Content Writing",
        "serve_08": "Social Media Management",
    }

    context = {'services': services,}
    return render(request,'services.html',context)