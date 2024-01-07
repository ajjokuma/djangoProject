from django.shortcuts import render
from .models import Eatery

def home(request):
    context = {
        'eateries': Eatery.objects.all()
    }
    return render(request, 'halalweb/home.html', context)

def about(request):
    return render(request, 'halalweb/about.html', {'title': 'About'})