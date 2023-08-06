from django.urls import path
from . import views

app_name = "blog"
urlpatterns = [
    path("authors/<int:auth_pk>/", views.author_articles, name="author_articles"),
    path("articles/<int:id>/", views.article_detail, name="article_detail"),
    path("authors/", views.add_author, name="add_author"),
    path("articles/", views.add_article, name="add_article"),
]
