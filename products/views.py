from django.shortcuts import render
from django.views.generic import ListView
from .models import Product

# Create your views here.

class Home(ListView):
    template_name = 'home-page copy.html'

    def get_queryset(self):
        return Product.objects.all().order_by('?')[:15]   

    


