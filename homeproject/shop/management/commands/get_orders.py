from typing import Any
from django.core.management.base import BaseCommand, CommandParser
from shop.models import Order, OrderLine


class Command(BaseCommand):
    help = "Show <n> orders. By default  - return all orders"

    def add_arguments(self, parser: CommandParser) -> None:
        parser.add_argument(
            "-n",
            "--count",
            type=int,
            required=False,
            help="Count customers to show",
        )
        parser.add_argument(
            "--last",
            required=False,
            choices=("True", "False"),
            default="True",
            help="If True get the latest orders, else get the very first orders. By default - True",
        )

    def handle(self, *args: Any, **options: Any) -> str | None:
        n_orders = options.get("count")
        ordering = "-" if options.get("last") == "True" else ""
        if n_orders:
            orders = Order.objects.all().order_by(f"{ordering}created")[:n_orders]
        else:
            orders = Order.objects.all().order_by(f"{ordering}created")

        self.stdout.write("Orders:")
        for order in orders:
            self.stdout.write(f"\n{order}: Total price: {order.total_price}")
            order_lines = order.order_lines.all()
            for p in order_lines:
                self.stdout.write(f"{p.product.title} {p.quantity} {p.product.price}")
