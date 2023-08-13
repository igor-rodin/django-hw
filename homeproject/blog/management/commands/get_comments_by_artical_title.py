from typing import Any
from django.core.management.base import BaseCommand, CommandParser
from blog.models import Comment


class Command(BaseCommand):
    help = "Get <n> conmments to artical <title>. By default <n> = 0 - returns all comments"

    def add_arguments(self, parser: CommandParser) -> None:
        parser.add_argument("title", type=str, help="Article title")

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
        article_title = options.get("title")
        order = "-" if options.get("last") == "True" else ""

        if n_comments:
            commments = Comment.objects.filter(article__title=article_title).order_by(
                f"{order}updated"
            )[:n_comments]
        else:
            commments = Comment.objects.filter(article__title=article_title).order_by(
                f"{order}updated"
            )
        self.stdout.write(f"{commments}")
