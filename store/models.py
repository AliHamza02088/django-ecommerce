from typing import Required
from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
    DEVICE_CHOICES = [
        ("Mobile", "Mobile"),
        ("Tablet", "Tablet"),
        ("Laptop",'Laptop'),
        ("Watch","Watch"),
        ("Gadget","Gadget"),
        ("Speaker","Speaker"),
        ("Accessories","Accessories"),
        ("Computer","Computer"),
    ]
    name = models.CharField(max_length=255, choices=DEVICE_CHOICES)
    
    def __str__(self):
        return self.name
    
class SubCategory(models.Model):
    name = models.CharField(max_length=255)
    category_id = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="main_category")
    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=255) 
    sku = models.CharField(max_length=100, unique=True)  
    category = models.ForeignKey(SubCategory, on_delete=models.CASCADE, related_name='products')
    warranty = models.CharField(max_length=255)  
    availability = models.CharField(max_length=100) 
    price = models.DecimalField(max_digits=10, decimal_places=2)
    original_price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)  
    discount = models.PositiveIntegerField(null=True, blank=True)  
    features = models.TextField()
    image_url = models.URLField(max_length=500, null=True, blank=True) 

    def __str__(self):
        return self.name
    
    
class Features(models.Model):
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255)

    
    def __str__(self):
        return self.name    
class ProductImage(models.Model):
    product = models.ForeignKey(Product, related_name='images', on_delete=models.CASCADE)
    image_url = models.URLField(max_length=500)

    def __str__(self):
        return f"Image for {self.product.name}"

class cart(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    pro_id = models.ForeignKey(Product, on_delete=models.CASCADE)
    image_url = models.ForeignKey(ProductImage, on_delete=models.CASCADE , null=True , blank=True)
    quantity = models.PositiveIntegerField(default=1)
    total = models.IntegerField(default=0)
    grand_total = models.IntegerField(default=0)
    
    def __str__(self):
        return f"{self.pro_id.name}, {self.quantity}"

    

class Address(models.Model):
    first_name = models.CharField(max_length=255 , null=True , blank=True)
    last_name = models.CharField(max_length=255 , null=True , blank=True )
    address = models.CharField(max_length=255)
    area_code = models.IntegerField()
    phone_number = models.IntegerField()
    zip_code = models.IntegerField()
    company = models.CharField(max_length=25 , null=True , blank=True)
    business = models.BooleanField(default=False)
    
    def __str__(self):
        return f'{self.first_name} {self.last_name}'