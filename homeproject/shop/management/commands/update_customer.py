import datetime
from django.core.management.base import BaseCommand
from shop.models import Customer


class Command(BaseCommand):
    help = "Update customer"

    def add_arguments(self, parser):
        parser.add_argument("id", type=int, help="Customer Id")
        parser.add_argument(
            "-n", "--name", type=str, required=False, help="Customer name"
        )
        parser.add_argument(
            "-p", "--phone", type=str, required=False, help="Customer phone number"
        )
        parser.add_argument(
            "-e", "--email", type=str, required=False, help="Customer email"
        )
        parser.add_argument(
            "-a", "--address", type=str, required=False, help="Customer address"
        )

    def handle(self, *args, **options):
        pk = options.get("id")
        customer = Customer.objects.filter(pk=pk).first()
        new_name = options.get("name")
        if new_name:
            customer.name = new_name

        new_phone = options.get("phone")
        if new_phone:
            customer.phone = new_phone

        new_email = options.get("email")
        if new_email:
            customer.email = new_email

        new_address = options.get("address")
        if new_address:
            customer.address = new_address

        customer.save()
        self.stdout.write(f"{customer}")
