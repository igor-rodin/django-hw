from django.db import models


# Create your models here.
class Author(models.Model):
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100, blank=True)
    email = models.EmailField(unique=True)
    biography = models.TextField(blank=True, null=True)
    birtday = models.DateField(blank=True, null=True)

    @property
    def full_name(self):
        return f"{self.name} {self.surname}"

    def __str__(self):
        return self.full_name


class Article(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    date_published = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(
        Author, on_delete=models.CASCADE, related_name="articles"
    )
    category = models.CharField(max_length=100)
    n_views = models.PositiveIntegerField(
        default=0, verbose_name="Количство просмотров"
    )
    is_published = models.BooleanField(default=False)

    def __str__(self):
        return f"Title: {self.title}, Author: {self.author.name}"

    class Meta:
        ordering = ["-date_published"]


class Comment(models.Model):
    comment = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(
        Author, on_delete=models.CASCADE, related_name="comments"
    )
    article = models.ForeignKey(
        Article, on_delete=models.CASCADE, related_name="comments"
    )

    def __str__(self) -> str:
        return f"{self.author.name} to Article {self.article.title} - {self.comment}"

    class Meta:
        ordering = ["-updated"]
