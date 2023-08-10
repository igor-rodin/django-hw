from django.contrib import admin

from .models import Article, Author, Comment


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ("title", "category", "date_published", "author", "n_views")
    ordering = ["-date_published", "author"]
    list_filter = ("date_published", "category")
    search_fields = ("title", "category", "author__name", "author__surname")
    search_help_text = "Поиск по pаголовку, категории и автору"
    fieldsets = [
        (
            None,
            {
                "classes": ["wide"],
                "fields": ["author", "title", "category", "date_published"],
            },
        ),
        ("Текст статьи", {"classes": ["collapse"], "fields": ["content"]}),
        (
            "Дополнительно",
            {"classes": ["collapse"], "fields": ["is_published", "n_views"]},
        ),
    ]
    readonly_fields = ["n_views", "date_published"]


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ("name", "surname", "email", "birtday")
    ordering = ["surname", "name"]
    search_fields = ("email", "name", "surname")
    search_help_text = "Поиск по имени и почте"
    fieldsets = [
        (None, {"classes": ["wide"], "fields": ["name", "surname"]}),
        ("Контакты", {"classes": ["collapse"], "fields": ["email"]}),
        ("Об авторе", {"classes": ["collapse"], "fields": ["birtday", "biography"]}),
    ]
    readonly_fields = ["birtday", "biography"]


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ("comment", "author", "article", "updated")
    ordering = ["-updated", "article"]
    search_fields = ("comment", "author__name")
    search_help_text = "Поиск по полю комментарий"
