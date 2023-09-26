from typing import Any
from django.core.management.base import BaseCommand, CommandParser
from productapp.management.commands.scrape import get_data
from productapp.models import Product


class Command(BaseCommand):
    
    def add_arguments(self, parser: CommandParser) -> None:
        pass
    
    def handle(self, *args: Any, **options: Any) -> str | None:
        
        product_data = get_data()

        product = Product(**product_data)
        product.save()