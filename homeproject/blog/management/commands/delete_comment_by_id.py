from typing import Any
from django.core.management.base import BaseCommand, CommandParser
from blog.models import Comment


class Command(BaseCommand):
    help = "Delete comment by id"

    def add_arguments(self, parser: CommandParser) -> None:
        parser.add_argument("id", type=int, help="Comment id")

    def handle(self, *args: Any, **options: Any) -> str | None:
        pk = options.get("id")
        comment = Comment.objects.filter(pk=pk).first()
        if comment:
            comment.delete()
        self.stdout.write(f"{comment}")
