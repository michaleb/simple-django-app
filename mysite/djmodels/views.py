#from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def djmodels(response):
    return HttpResponse("Hello, this is my first django models app")