import datetime
from decimal import Decimal
from django.core.management.base import BaseCommand
from shop.models import Product


class Command(BaseCommand):
    help = "Update product"

    def add_arguments(self, parser):
        parser.add_argument("id", type=int, help="Product Id")
        parser.add_argument(
            "-t", "--title", type=str, required=False, help="Product title"
        )
        parser.add_argument(
            "-d", "--desc", type=str, required=False, help="Product description"
        )
        parser.add_argument(
            "-p", "--price", type=Decimal, required=False, help="Product price"
        )
        # parser.add_argument(
        #     "-c", "--count", type=int, required=False, help="Product quantity"
        # )

    def handle(self, *args, **options):
        pk = options.get("id")
        product = Product.objects.filter(pk=pk).first()
        new_name = options.get("title")
        if new_name:
            product.title = new_name

        new_description = options.get("desc")
        if new_description:
            product.description = new_description

        new_price = options.get("price")
        if new_price:
            product.price = new_price

        # new_count = options.get("count")
        # if new_count:
        #     product.quantity = new_count

        product.save()
        self.stdout.write(f"{product}")
