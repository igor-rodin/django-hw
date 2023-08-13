from typing import Any
from django.core.management.base import BaseCommand, CommandParser
from shop.models import Customer


class Command(BaseCommand):
    help = "Get customer by name"

    def add_arguments(self, parser: CommandParser) -> None:
        parser.add_argument("name", type=str, help="Customer name")

    def handle(self, *args: Any, **options: Any) -> str | None:
        name = options.get("name")
        customer = Customer.objects.filter(name__icontains=name)
        self.stdout.write(f"{customer}")
