from typing import Any
from django.core.management.base import BaseCommand, CommandParser
from blog.models import Article


class Command(BaseCommand):
    help = "Show last <n> articals. By default <n> = 0 - returns all artcals"

    def add_arguments(self, parser: CommandParser) -> None:
        parser.add_argument(
            "--count", type=int, required=False, help="Count articals to show"
        )

    def handle(self, *args: Any, **options: Any) -> str | None:
        n_articals = options.get("count")
        if n_articals:
            articals = Article.objects.all()[:n_articals]
        else:
            articals = Article.objects.all()
        self.stdout.write(f"{articals}")
