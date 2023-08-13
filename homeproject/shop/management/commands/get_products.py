from typing import Any
from django.core.management.base import BaseCommand, CommandParser
from shop.models import Product


class Command(BaseCommand):
    help = "Show <n> products. By default returns all products"

    def add_arguments(self, parser: CommandParser) -> None:
        parser.add_argument(
            "-n", "--count", type=int, required=False, help="Count customers to show"
        )

    def handle(self, *args: Any, **options: Any) -> str | None:
        n_products = options.get("count")
        if n_products:
            products = Product.objects.all().order_by("title")[:n_products]
        else:
            products = Product.objects.all().order_by("title")
        self.stdout.write(f"{products}")
