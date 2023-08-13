from django.core.management.base import BaseCommand
from shop.models import Customer


class Command(BaseCommand):
    help = "Create customer."

    def add_arguments(self, parser):
        parser.add_argument("name", type=str, help="Customer name")
        parser.add_argument("email", type=str, help="Customer email")
        parser.add_argument("phone", type=str, help="Customer phone number")
        parser.add_argument("address", type=str, help="Customer address")

    def handle(self, *args, **options):
        customer = Customer(
            name=options.get("name"),
            email=options.get("email"),
            phone=options.get("phone"),
            address=options.get("address"),
        )
        customer.save()
        self.stdout.write(f"{customer}")
