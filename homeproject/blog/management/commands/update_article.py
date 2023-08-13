from django.core.management.base import BaseCommand
from blog.models import Article


class Command(BaseCommand):
    help = "Update artical"

    def add_arguments(self, parser):
        parser.add_argument("id", type=int, help="Artical Id")
        parser.add_argument("--title", type=str, required=False, help="Artical title")
        parser.add_argument(
            "--content", type=str, required=False, help="Artical content"
        )
        parser.add_argument("--category", type=str, required=False, help="Category")
        parser.add_argument(
            "--published", type=bool, required=False, help="Is Published"
        )

    def handle(self, *args, **options):
        pk = options.get("id")
        artical = Article.objects.filter(pk=pk).first()
        new_title = options.get("title")
        if new_title:
            artical.title = new_title

        new_content = options.get("content")
        if new_content:
            artical.content = new_content

        new_category = options.get("category")
        if new_category:
            artical.category = new_category

        new_pub = options.get("published")
        if new_pub:
            artical.is_published = new_pub

        artical.save()
        self.stdout.write(f"{artical}")
