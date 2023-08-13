from typing import Any
from django.core.management.base import BaseCommand, CommandParser
from blog.models import Comment


class Command(BaseCommand):
    help = (
        "Get <n> conmments for author <name>. By default <n> = 0 - returns all articles"
    )

    def add_arguments(self, parser: CommandParser) -> None:
        parser.add_argument("name", type=str, help="Author name")

        parser.add_argument(
            "-n", "--number", type=int, required=False, help="Number comments to show"
        )
        parser.add_argument(
            "--last",
            required=False,
            choices=("True", "False"),
            default="True",
            help="If True get the latest comments, else get the very first comments. By default - True",
        )

    def handle(self, *args: Any, **options: Any) -> str | None:
        n_comments = options.get("number")
        author_name = options.get("name")
        order = "-" if options.get("last") == "True" else ""

        if n_comments:
            commments = Comment.objects.filter(author__name=author_name).order_by(
                f"{order}updated"
            )[:n_comments]
        else:
            commments = Comment.objects.filter(author__name=author_name).order_by(
                f"{order}updated"
            )
        self.stdout.write(f"{commments}")
