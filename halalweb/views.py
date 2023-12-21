from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return HttpResponse('<h1>Halal Web Home<h1>')

def about(request):
    return HttpResponse('<h1>Halal Web About<h1>')