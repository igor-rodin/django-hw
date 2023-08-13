from typing import Any
from django.core.management.base import BaseCommand, CommandParser
from shop.models import Order


class Command(BaseCommand):
    help = "Delete order by id"

    def add_arguments(self, parser: CommandParser) -> None:
        parser.add_argument("id", type=int, help="Order id")

    def handle(self, *args: Any, **options: Any) -> str | None:
        pk = options.get("id")
        order = Order.objects.filter(pk=pk).first()
        if order:
            order.delete()
        self.stdout.write(f"{order}")
