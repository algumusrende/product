from productapp.management.commands.scrape import get_data
from productapp.models import Product

product_data = get_data()

product = Product(**product_data)
product.save()