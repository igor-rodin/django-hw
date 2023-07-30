from typing import Any
from django.core.management.base import BaseCommand, CommandParser
from blog.models import Author


class Command(BaseCommand):
    help = "Show last <n> authors. By default <n> = 0 - returns all authors"

    def add_arguments(self, parser: CommandParser) -> None:
        parser.add_argument(
            "--count", type=int, required=False, help="Count authors to show"
        )

    def handle(self, *args: Any, **options: Any) -> str | None:
        n_authors = options.get("count")
        if n_authors:
            authors = Author.objects.all()[:n_authors]
        else:
            authors = Author.objects.all()
        self.stdout.write(f"{authors}")
