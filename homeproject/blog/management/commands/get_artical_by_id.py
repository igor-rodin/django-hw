from typing import Any
from django.core.management.base import BaseCommand, CommandParser
from blog.models import Article


class Command(BaseCommand):
    help = "Get artical by Id"

    def add_arguments(self, parser: CommandParser) -> None:
        parser.add_argument("id", type=int, help="Artical Id")

    def handle(self, *args: Any, **options: Any) -> str | None:
        pk = options.get("id")
        artical = Article.objects.filter(pk=pk).first()
        self.stdout.write(f"{artical}")
