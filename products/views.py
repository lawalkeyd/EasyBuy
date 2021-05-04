from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from .models import Product

# Create your views here.

class Home(ListView):
    """
    Homepage View, Returns 15 random products
    """
    template_name = 'home-page.html'
    context_object_name = 'items'

    def get_queryset(self):
        return Product.objects.all().order_by('?')[:15] 

class ProductItem(DetailView):
    """
    Product detail view
    """
    model = Product     
    template_name='products/product_item.html'
    context_object_name = "details"

    def get_object(self, queryset=None):
        slug = self.kwargs['slug']
        a_obj = Product.objects.get(id=slug)
        return a_obj

    


