from typing import Any
from django.core.management.base import BaseCommand, CommandParser
from shop.models import Customer


class Command(BaseCommand):
    help = "Delete customer by id"

    def add_arguments(self, parser: CommandParser) -> None:
        parser.add_argument("id", type=int, help="Customer id")

    def handle(self, *args: Any, **options: Any) -> str | None:
        pk = options.get("id")
        customer = Customer.objects.filter(pk=pk).first()
        if customer:
            customer.delete()
        self.stdout.write(f"{customer}")
