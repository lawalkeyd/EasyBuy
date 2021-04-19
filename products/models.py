from django.db import models
from datetime import date

# Create your models here.

class CompanyStore(models.Model):
    name = models.CharField(max_length=84)
    location = models.CharField(max_length=54)
    description = models.TextField()

class Category(models.Model):
    name = models.CharField(max_length=24, unique=True) 

    def __str__(self):
        return self.name 

label_choices = (
    ('null', ' '),
    ('success', 'new'),
    ('primary', 'bestseller'),
)

class Product(models.Model):
    title = models.CharField(max_length=40)
    category = models.ForeignKey(Category, on_delete=models.PROTECT)
    store = models.ForeignKey(CompanyStore, on_delete=models.CASCADE)
    price = models.FloatField()
    discount_price = models.FloatField(null=True, blank=True)
    photo = models.ImageField(upload_to='store-photos/', blank=False, null=True)
    description = models.TextField()
    label = models.CharField(max_length=17, choices=label_choices)
    currently_available = models.BooleanField(default=True)
    next_available_date = models.DateField(default=date.today, blank=True)

    def __str__(self):
        return self.title  

    class Meta:
        unique_together = ['title', 'store']    
