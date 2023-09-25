from django.contrib import admin
from .models import Product

# Register your models here.
class ProductAdmin(admin.ModelAdmin):
    list_display= ('id', 'name', 'brand', 'selling_price', 'discounted_price', 'category', 'merchant_info', 'other_merchants')
    
  
admin.site.register(Product, ProductAdmin)
