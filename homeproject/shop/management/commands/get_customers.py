from typing import Any
from django.core.management.base import BaseCommand, CommandParser
from shop.models import Customer


class Command(BaseCommand):
    help = "Show <n> customers. By default return all customers"

    def add_arguments(self, parser: CommandParser) -> None:
        parser.add_argument(
            "-n",
            "--count",
            type=int,
            required=False,
            help="Count customers to show",
        )

    def handle(self, *args: Any, **options: Any) -> str | None:
        n_customers = options.get("count")
        if n_customers:
            customers = Customer.objects.all().order_by("name")[:n_customers]
        else:
            customers = Customer.objects.all().order_by("name")
        self.stdout.write(f"{customers}")
