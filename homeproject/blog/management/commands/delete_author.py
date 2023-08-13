from typing import Any
from django.core.management.base import BaseCommand, CommandParser
from blog.models import Author


class Command(BaseCommand):
    help = "Delete author by Id"

    def add_arguments(self, parser: CommandParser) -> None:
        parser.add_argument("id", type=int, help="Author Id")

    def handle(self, *args: Any, **options: Any) -> str | None:
        pk = options.get("id")
        author = Author.objects.filter(pk=pk).first()
        if author:
            author.delete()
        self.stdout.write(f"{author}")
