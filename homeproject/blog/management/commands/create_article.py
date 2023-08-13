from django.core.management.base import BaseCommand
from blog.models import Article, Author


class Command(BaseCommand):
    help = "Create artical"

    def add_arguments(self, parser):
        parser.add_argument("title", type=str, help="Artical title")
        parser.add_argument("content", type=str, help="Artical content")
        parser.add_argument("category", type=str, help="Category")
        parser.add_argument("author_id", type=int, help="Author Id")

    def handle(self, *args, **options):
        auth_pk = options.get("author_id")
        author = Author.objects.filter(pk=auth_pk).first()
        artical = None
        if author:
            artical = Article(
                title=options.get("title"),
                content=options.get("content"),
                category=options.get("category"),
                author=author,
            )
            artical.save()
        self.stdout.write(f"{artical}")
