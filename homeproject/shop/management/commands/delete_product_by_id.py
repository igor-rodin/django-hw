from typing import Any
from django.core.management.base import BaseCommand, CommandParser
from shop.models import Product


class Command(BaseCommand):
    help = "Delete product by id"

    def add_arguments(self, parser: CommandParser) -> None:
        parser.add_argument("id", type=int, help="Comment id")

    def handle(self, *args: Any, **options: Any) -> str | None:
        pk = options.get("id")
        product = Product.objects.filter(pk=pk).first()
        if product:
            product.delete()
        self.stdout.write(f"{product}")
