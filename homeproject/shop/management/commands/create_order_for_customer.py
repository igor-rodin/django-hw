from django.core.management.base import BaseCommand
from shop.models import Customer, Product, Order


class Command(BaseCommand):
    help = "Create order for customer by <email> with list of products <product_id> ."

    def add_arguments(self, parser):
        parser.add_argument("email", type=str, help="Customer email")
        parser.add_argument("ids", type=int, nargs="+", help="List of product id")

    def handle(self, *args, **options):
        cust_email = options.get("email")
        product_ids = options.get("ids")
        order = None
        customer = Customer.objects.filter(email=cust_email).first()
        if customer:
            products = Product.objects.filter(pk__in=product_ids)
            if products:
                order = Order.objects.create(customer=customer)
                order.products.add(*products)

        self.stdout.write(f"{order}: Total price: {order.total_price}")
        for p in order.products.all():
            self.stdout.write(f"{p.title} {p.quantity} {p.price}")
