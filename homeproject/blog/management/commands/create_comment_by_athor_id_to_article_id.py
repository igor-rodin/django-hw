from django.core.management.base import BaseCommand
from blog.models import Article, Author, Comment


class Command(BaseCommand):
    help = "Create comment by author <author_id> to article <article_id>"

    def add_arguments(self, parser):
        parser.add_argument("author_id", type=int, help="Author id")
        parser.add_argument("article_id", type=int, help="Artcle id")
        parser.add_argument("comment", type=str, help="Comment content")

    def handle(self, *args, **options):
        auth_pk = options.get("author_id")
        article_pk = options.get("article_id")
        author = Author.objects.filter(pk=auth_pk).first()
        article = Article.objects.filter(pk=article_pk).first()
        comment = None
        if author and article:
            comment = Comment(
                comment=options.get("comment"),
                author=author,
                article=article,
            )
            comment.save()
        self.stdout.write(f"{comment}")
