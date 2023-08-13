import datetime
from django.core.management.base import BaseCommand
from blog.models import Author


class Command(BaseCommand):
    help = "Update author"

    def add_arguments(self, parser):
        parser.add_argument("id", type=int, help="Artical Id")
        parser.add_argument("--name", type=str, required=False, help="Author name")
        parser.add_argument(
            "--surname", type=str, required=False, help="Author surname"
        )
        parser.add_argument("--email", type=str, required=False, help="Author email")
        parser.add_argument(
            "--biography", type=str, required=False, help="Author biography"
        )
        parser.add_argument(
            "--birthday",
            type=lambda d: datetime.datetime.strptime(d, "%Y-%m-%d").date(),
            required=False,
            help="Author birthday",
        )

    def handle(self, *args, **options):
        pk = options.get("id")
        author = Author.objects.filter(pk=pk).first()
        new_name = options.get("name")
        if new_name:
            author.name = new_name

        new_surname = options.get("surname")
        if new_surname:
            author.surname = new_surname

        new_email = options.get("email")
        if new_email:
            author.email = new_email

        new_biography = options.get("biography")
        if new_biography:
            author.biography = new_biography

        new_birthday = options.get("birthday")
        if new_birthday:
            author.birtday = new_birthday

        author.save()
        self.stdout.write(f"{author}")
