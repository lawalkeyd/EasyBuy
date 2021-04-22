from django.shortcuts import render
from django.views.generic import ListView
from .models import Product

# Create your views here.

class Home(ListView):
    template_name = 'home-page.html'
    context_object_name = 'items'

    def get_queryset(self):
        return Product.objects.all().order_by('?')[:15]   

    


