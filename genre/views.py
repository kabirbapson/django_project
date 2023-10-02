from django.shortcuts import render
from django.http import HttpResponse
from .models import Collections, Piece

# Create your views here.

def index(request):
    all_collection = Collections.objects.all()
    bello = 'Halima Bello'
    context = {
        'all_collection': all_collection,
        'bello': bello,
    }
    # print(all_collection)  # Debugging: Print the contents of all_collection
    return render(request, "genre/index.html", context)

def details(request, genre_id):
    cItem = Collections.objects.get(pk=genre_id)
    pItem = Piece.objects.filter(collection = cItem)
    context = {
        'pItem': pItem
    }
    print('my doe ',pItem)
    return render(request, 'genre/details.html', context)
