from django.db import models
from products.models import Product
from users.models import CustomUser

# Create your models here.
class OrderItem(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='order_items')
    item = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    ordered = models.BooleanField(default=False)

    def __str__(self):
        return str(self.quantity) + ' of ' + self.item.title + ' Order Item'
        
    def get_total_item_price(self):
        return self.quantity * self.item.price 

    def get_total_discount_item_price(self):
        return self.quantity * self.item.discount_price 

    def amount_saved(self):
        return self.item.price - self.item.discount_price

    def get_final_price(self):
        if self.item.discount_price:
            return self.get_total_discount_item_price()
        else:
            return self.get_total_item_price() 
               

class Order(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='orders')
    items = models.ManyToManyField(OrderItem)
    start_date = models.DateTimeField(auto_now_add=True)
    ordered_date = models.DateTimeField()
    ordered = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username + ' Order'

    def total_price(self):
        total = 0
        for item in self.items.all():
            total += item.get_final_price()
        return total    