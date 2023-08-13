import datetime
from django.core.management.base import BaseCommand
from blog.models import Author


class Command(BaseCommand):
    help = "Create author."

    def add_arguments(self, parser):
        parser.add_argument("name", type=str, help="Author name")
        parser.add_argument("surname", type=str, help="Author surname")
        parser.add_argument("email", type=str, help="Author email")
        parser.add_argument(
            "--biography", type=str, required=False, help="Author biography"
        )
        parser.add_argument(
            "--birtday",
            type=lambda d: datetime.datetime.strptime(d, "%Y-%m-%d").date(),
            required=False,
            help="Author birtday",
        )

    def handle(self, *args, **options):
        author = Author(
            name=options.get("name"),
            surname=options.get("surname"),
            email=options.get("email"),
            biography=options.get("biography"),
            birtday=options.get("birtday"),
        )
        author.save()
        self.stdout.write(f"{author}")
