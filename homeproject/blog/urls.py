from django.urls import path
from . import views

app_name = "blog"
urlpatterns = [
    path("authors/<int:auth_pk>/", views.author_articles, name="author_articles"),
    path("articles/<int:id>/", views.article_detail, name="article_detail"),
    path("authors/add/", views.add_author, name="add_author"),
    path("articles/add/", views.add_article, name="add_article"),
    path("authors/add/", views.add_author, name="add_author"),
    path("articles/", views.ArticlesView.as_view(), name="all_articles"),
]
