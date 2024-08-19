from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

services_data = [
    {
        'icon': 'python.png',
        'title': 'Web Development',
        'description': 'We provide web development services in Python (Django), MERN Stack'
    },
    # {
    #     'icon': 'android.png',
    #     'title': 'Mobile Development',
    #     'description': 'We provide mobile app development services in full stack android JAVA, Kotlin and Google Material'
    # },
    # {
    #     'icon': 'photoshop.png',
    #     'title': 'Graphic Designing',
    #     'description': 'One stop solution for all your graphic design needs'
    # },
    # {
    #     'icon': 'photoshop.png',
    #     'title': 'Graphic Designing',
    #     'description': 'One stop solution for all your graphic design needs'
    # },
    # {
    #     'icon': 'photoshop.png',
    #     'title': 'Graphic Designing',
    #     'description': 'One stop solution for all your graphic design needs'
    # },
    # {
    #     'icon': 'photoshop.png',
    #     'title': 'Graphic Designing',
    #     'description': 'One stop solution for all your graphic design needs'
    # }
]

def home(request):
    context = {
        'title': 'Home Page',
        'about': """ I am a full stack developer having 6+ years of experience. My area of expertise are HTML, CSS, JS, PHP, Laravel, MySQL, MongoDB, React, Node,
            Express, Android, Java, Kotlin, Python, Django""",
        'services': services_data
    }
    return render(request, 'portfolio/home.html', context)

def about(request):
    context = {
        'title': 'About Page',
        'services': services_data
    }
    return render(request, 'portfolio/about.html', context)

def services(request):
    context = {
        'title': 'Services Page',
        'services': services_data
    }
    return render(request, 'portfolio/services.html', context)

def contact(request):
    return render(request, 'portfolio/contact.html')