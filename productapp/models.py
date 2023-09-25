from django.db import models
# Create your models here.

class Product(models.Model):
    id =    models.BigAutoField(primary_key=True, editable=False)
    name = models.CharField(max_length=255)
    brand = models.CharField(max_length=100)
    selling_price = models.DecimalField(max_digits=10, decimal_places=2)
    discounted_price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.CharField(max_length=255)
    merchant_info = models.CharField(max_length=100)
    other_merchants = models.CharField(max_length=255)


