from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render
from django.http import HttpResponse
from .models import Collections, Piece
from django.views import generic
from django.views.generic import View
from .forms import UserForm
# Create your views here.

class index(generic.ListView):
    template_name = 'genre/index.html'

    def get_queryset(self):
        return Collections.objects.all()
    
class details(generic.DetailView):
    model = Collections
    template_name = 'genre/details.html'

class UserFormView(View):
    form_class = UserForm
    template_name = 'genre/form.html'

    def get(self, request):
        form = self.form_class(None)
        return render(request, self.template_name, {'form': form})
    
    def post(self, request):
        form = self.form_class(request.POST)

        if form.is_valid():
            

            
# def index(request):
#     all_collection = Collections.objects.all()
#     bello = 'Halima Bello'
#     context = {
#         'all_collection': all_collection,
#         'bello': bello,
#     }
#     # print(all_collection)  # Debugging: Print the contents of all_collection
#     return render(request, "genre/index.html", context)

# def details(request, genre_id):
#     cItem = Collections.objects.get(pk=genre_id)
#     pItem = Piece.objects.filter(collection = cItem)
#     context = {
#         'pItem': pItem
#     }
#     print('my doe ',pItem)
#     return render(request, 'genre/details.html', context)
