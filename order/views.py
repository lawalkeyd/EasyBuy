from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ObjectDoesNotExist
from products.models import Product, Category
from .forms import *
from django.contrib import messages
from django.utils import timezone

# Create your views here.
@login_required(login_url='account_login')
def ViewCheckout(request):
    order = get_object_or_404(Order, user=request.user, ordered=False)
    context = {
        'order': order,
    }   
    return render(request, 'order/checkout-page.html', context)

@login_required(login_url='account_login')
def add_to_cart(request):
    if request.method == 'POST':
        id = request.POST['id']
        quantity = request.POST['quantity']
    else:
        messages.error(request, 'Could not perform action')
        redirect('home')    
    item = get_object_or_404(Product, id=id)
    order_item, created = OrderItem.objects.get_or_create(
        item=item,
        user=request.user,
        ordered=False
    )
    order_qs = Order.objects.filter(user=request.user, ordered=False)
    if order_qs.exists():
        order = order_qs[0]
        # check if the order item is in the order
        if order.items.filter(item__id=item.id).exists():
            order_item.quantity += quantity
            order_item.save()
            messages.info(request, "This item quantity was updated.")
            return redirect("product_item", slug=id)
        else:
            order.items.add(order_item)
            messages.info(request, "This item was added to your cart.")
            return redirect("product_item", slug=id)
    else:
        ordered_date = timezone.now()
        order = Order.objects.create(
            user=request.user, ordered_date=ordered_date)
        order.items.add(order_item)
        messages.info(request, "This item was added to your cart.")
        return redirect("product-item", id=id)    

@login_required(login_url='account_login')
def remove_from_cart(request):
    if request.method == 'POST':
        id = request.POST['id']
    else:
        messages.error(request, 'Could not perform action')
        redirect('home')    
    item = get_object_or_404(Item, id=id)
    order_qs = Order.objects.filter(
        user=request.user,
        ordered=False
    )
    if order_qs.exists():
        order = order_qs[0]
        # check if the order item is in the order
        if order.items.filter(item__id=item.id).exists():
            order_item = OrderItem.objects.filter(
                item=item,
                user=request.user,
                ordered=False
            )[0]
            order.items.remove(order_item)
            order_item.delete()
            messages.info(request, "This item was removed from your cart.")
            return redirect("order-summary")
        else:
            messages.info(request, "This item was not in your cart")
            return redirect("view-store-item", id=id)
    else:
        messages.info(request, "You do not have an active order")
        return redirect("view-store-item", id=id)     

@login_required(login_url='account_login')
def OrderSummary(request):
    try:
        order = Order.objects.get(user=request.user, ordered=False)
    except ObjectDoesNotExist:
        messages.error(request, 'You do not have an active Order')
        return redirect('/')
    context = {
        'order': order
    }    
    return render(request, 'order/order-summary.html', context)    

