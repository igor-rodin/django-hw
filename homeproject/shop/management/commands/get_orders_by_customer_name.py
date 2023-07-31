from typing import Any
from django.core.management.base import BaseCommand, CommandParser
from shop.models import Order


class Command(BaseCommand):
    help = "Show <n> orders for customer <name>. By default returns all"

    def add_arguments(self, parser: CommandParser) -> None:
        parser.add_argument("name", type=str, help="Customer name")
        parser.add_argument(
            "-n",
            "--count",
            type=int,
            required=False,
            help="Count orders to show",
        )
        parser.add_argument(
            "--last",
            required=False,
            choices=("True", "False"),
            default="True",
            help="If True get the latest orders, else get the very first orders. By default - True",
        )

    def handle(self, *args: Any, **options: Any) -> str | None:
        customer_name = options.get("name")
        n_orders = options.get("count")
        ordering = "-" if options.get("last") == "True" else ""
        if n_orders:
            orders = Order.objects.filter(
                customer__name__icontains=customer_name
            ).order_by(f"{ordering}created")[:n_orders]
        else:
            orders = Order.objects.filter(
                customer__name__icontains=customer_name
            ).order_by(f"{ordering}created")

        self.stdout.write("Orders:")
        for order in orders:
            self.stdout.write(f"\n{order}: Total price: {order.total_price}")
            for p in order.products.all():
                self.stdout.write(f"{p.title} {p.quantity} {p.price}")
