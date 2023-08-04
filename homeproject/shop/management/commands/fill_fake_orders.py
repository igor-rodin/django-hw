import datetime
from typing import Any
from django.core.management.base import BaseCommand, CommandParser
from shop.models import Product, Customer, Order, OrderLine
import random


class Command(BaseCommand):
    help = "Fill db with fakes data"

    def add_arguments(self, parser: CommandParser) -> None:
        parser.add_argument(
            "-o",
            "--orders",
            type=int,
            required=False,
            default=10,
            help="Number of fake orders",
        )
        parser.add_argument(
            "-c",
            "--cust",
            type=int,
            required=False,
            default=10,
            help="Number of fake customers",
        )
        parser.add_argument(
            "-p",
            "--product",
            type=int,
            required=False,
            default=10,
            help="Number of fake products",
        )

    def handle(self, *args: Any, **options: Any) -> str | None:
        n_orders = options.get("orders")
        n_customers = options.get("cust")
        n_products = options.get("product")

        order_lines = OrderLine.objects.all()
        if order_lines:
            order_lines.delete()

        orders = Order.objects.all()
        if orders:
            orders.delete()

        products = Product.objects.all()
        if products:
            products.delete()

        customers = Customer.objects.all()
        if customers:
            customers.delete()

        for i in range(1, n_customers + 1):
            customer = Customer(
                name=f"Customer-{i}",
                email=f"cust-{i}@mail.com",
                phone=f"+79009090088",
                address=f"Address-{i}",
            )
            customer.save()

        for i in range(1, n_products + 1):
            product = Product(
                title=f"Product-{i}",
                price=random.uniform(100.0, 500_000.0),
            )
            product.save()

        customers = Customer.objects.all()
        products = Product.objects.all()

        for i in range(1, n_orders + 1):
            rnd_cust = random.choice(customers)
            order = Order.objects.create(customer=rnd_cust)
            order.created = datetime.datetime(
                random.randint(2021, 2023), random.randint(1, 12), random.randint(1, 30)
            )
            order.save()

            rnd_prod = random.choices(products, k=random.randrange(1, n_products))
            for p in rnd_prod:
                OrderLine.objects.create(
                    order=order, product=p, quantity=random.randint(1, 5)
                )

        self.stdout.write("Data filled...")
