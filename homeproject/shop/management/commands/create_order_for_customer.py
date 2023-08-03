import datetime
from django.core.management.base import BaseCommand
from shop.models import Customer, Product, Order, OrderLine


class Command(BaseCommand):
    help = "Create order for customer by <email> with list of products <product_id> and list of <products_count>."

    def add_arguments(self, parser):
        parser.add_argument("email", type=str, help="Customer email")
        parser.add_argument(
            "-a",
            "--added",
            type=lambda d: datetime.datetime.strptime(d, "%Y-%m-%d"),
            required=False,
            help="Order added",
        )
        parser.add_argument(
            "-i",
            "--id",
            type=int,
            nargs="+",
            action="append",
            help="List of product id",
        )
        parser.add_argument(
            "-c",
            "--count",
            type=int,
            nargs="+",
            action="append",
            help="List of product quntities",
        )

    def handle(self, *args, **options):
        cust_email = options.get("email")
        product_ids = [id[0] for id in options.get("id")]
        product_counts = [id[0] for id in options.get("count")]
        customer = Customer.objects.filter(email=cust_email).first()
        added = options.get("added")
        order = Order.objects.create(customer=customer)
        order.created = added
        order.save()
        if customer:
            products = Product.objects.filter(pk__in=product_ids)
            if products:
                self.stdout.write(f"{products}")
                for i in range(products.count()):
                    OrderLine.objects.create(
                        order=order, product=products[i], quantity=product_counts[i]
                    )
        self.stdout.write(f"{order}: Total price: {order.total_price}")
        order_lines = OrderLine.objects.filter(order=order)
        for p in order_lines.all():
            self.stdout.write(f"{p.product.title} {p.quantity} {p.product.price}")
