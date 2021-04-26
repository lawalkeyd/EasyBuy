from django.urls import path
from .views import ProductItem

urlpatterns = [
    path('<slug:slug>', ProductItem.as_view(), name='product_item'),
]