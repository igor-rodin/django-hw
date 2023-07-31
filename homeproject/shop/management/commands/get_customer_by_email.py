from typing import Any
from django.core.management.base import BaseCommand, CommandParser
from shop.models import Customer


class Command(BaseCommand):
    help = "Get customer by email"

    def add_arguments(self, parser: CommandParser) -> None:
        parser.add_argument("email", type=str, help="Customer email")

    def handle(self, *args: Any, **options: Any) -> str | None:
        email = options.get("email")
        customer = Customer.objects.filter(email=email).first()
        self.stdout.write(f"{customer}")
