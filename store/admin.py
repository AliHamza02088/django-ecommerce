from django.contrib import admin
from .models import Product, Category , Features , ProductImage , SubCategory
# Register your models here.
admin.site.register(Product)
admin.site.register(Category)
admin.site.register(Features)
admin.site.register(ProductImage)
admin.site.register(SubCategory)