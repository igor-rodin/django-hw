from typing import Any
from django.core.management.base import BaseCommand, CommandParser
from blog.models import Article


class Command(BaseCommand):
    help = (
        "Get <n> articles for author <name>. By default <n> = 0 - returns all articles"
    )

    def add_arguments(self, parser: CommandParser) -> None:
        parser.add_argument("name", type=str, help="Aythor name")

        parser.add_argument(
            "-n", "--number", type=int, required=False, help="Number articles to show"
        )
        parser.add_argument(
            "--last",
            required=False,
            choices=("True", "False"),
            default="True",
            help="If True get the latest articles, else get the very first articles. By default - True",
        )

    def handle(self, *args: Any, **options: Any) -> str | None:
        n_articles = options.get("number")
        author_name = options.get("name")
        order = "-" if options.get("last") == "True" else ""

        if n_articles:
            articles = Article.objects.filter(author__name=author_name).order_by(
                f"{order}date_published"
            )[:n_articles]
        else:
            articles = Article.objects.filter(author__name=author_name).order_by(
                f"{order}date_published"
            )
        self.stdout.write(f"{articles}")
