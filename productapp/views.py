from django.shortcuts import render
from .models import Product
from ..scrape import product_data


Product.objects.create(**product_data)



