from django.urls import path
from . import views

urlpatterns = [
   path('checkout/', views.ViewCheckout, name='view-checkout'),
   path('order-summary', views.OrderSummary, name='order-summary'),
   path('remove-item', views.remove_from_cart, name='remove-from-cart'), 
   path('add-to-cart/', views.add_to_cart, name='add-to-cart'),  
]