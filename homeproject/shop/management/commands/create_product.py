from decimal import Decimal
from django.core.management.base import BaseCommand
from shop.models import Product


class Command(BaseCommand):
    help = "Create product."

    def add_arguments(self, parser):
        parser.add_argument("title", type=str, help="Prooduct title")
        parser.add_argument("price", type=Decimal, help="Product price")
        parser.add_argument("quantity", type=int, help="Product quantity")
        parser.add_argument(
            "-d", "--description", type=str, required=False, help="Product description"
        )

    def handle(self, *args, **options):
        product = Product(
            title=options.get("title"),
            price=options.get("price"),
            quantity=options.get("quantity"),
        )
        desc = options.get("description")
        if desc:
            product.description = desc
        product.save()
        self.stdout.write(f"{product}")
