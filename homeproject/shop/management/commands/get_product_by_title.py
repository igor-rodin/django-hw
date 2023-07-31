from typing import Any
from django.core.management.base import BaseCommand, CommandParser
from shop.models import Product


class Command(BaseCommand):
    help = "Get products by title"

    def add_arguments(self, parser: CommandParser) -> None:
        parser.add_argument("title", type=str, help="Product title")

    def handle(self, *args: Any, **options: Any) -> str | None:
        title = options.get("title")
        product = Product.objects.filter(title__icontains=title)
        self.stdout.write(f"{product}")
