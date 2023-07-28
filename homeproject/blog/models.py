from django.db import models


# Create your models here.
class Author(models.Model):
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    biography = models.TextField(blank=True)
    birtday = models.DateField(blank=True)

    @property
    def full_name(self):
        return f"{self.name} {self.surname}"

    def __str__(self):
        return self.full_name


class Article(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    date_published = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    category = models.CharField(max_length=100)
    n_views = models.PositiveIntegerField(
        default=0, verbose_name="Количство просмотров"
    )
    is_published = models.BooleanField(default=False)

    def __str__(self):
        return f"Title: {self.title}"

    class Meta:
        ordering = ["-date_published"]
