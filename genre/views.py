from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(response):
    return HttpResponse('<h1>Hello baps hhere</h1>')

def details(response, genre_id):
    return HttpResponse('<h2>Genre ID is: ' + str(genre_id) + '</h2>')