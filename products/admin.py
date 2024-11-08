from django.contrib import admin

from .models import Product

# Register your models here.

class ProductAdmin(admin.ModelAdmin):
    model=Product
    list_display=['name','price','date_creation']
    search_fields=['name','price','date_creation']
    
admin.site.register(Product, ProductAdmin)
    