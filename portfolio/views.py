from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

services = [
    {
        'icon': 'python.png',
        'title': 'Web Development',
        'description': 'We provide web development services in Python (Django), MERN Stack'
    },
    {
        'icon': 'android.png',
        'title': 'Mobile Development',
        'description': 'We provide mobile app development services in full stack android JAVA, Kotlin and Google Material'
    },
    {
        'icon': 'photoshop.png',
        'title': 'Graphic Designing',
        'description': 'One stop solution for all your graphic design needs'
    },
    {
        'icon': 'photoshop.png',
        'title': 'Graphic Designing',
        'description': 'One stop solution for all your graphic design needs'
    },
    {
        'icon': 'photoshop.png',
        'title': 'Graphic Designing',
        'description': 'One stop solution for all your graphic design needs'
    },
    {
        'icon': 'photoshop.png',
        'title': 'Graphic Designing',
        'description': 'One stop solution for all your graphic design needs'
    }
]

def home(request):
    context = {
        'services': services
    }
    return render(request, 'portfolio/home.html', context)

def about(request):
    context = {
        'services': services
    }
    return render(request, 'portfolio/about.html', context)

def contact(request):
    return HttpResponse('<h1>My Contact Page</h1>')