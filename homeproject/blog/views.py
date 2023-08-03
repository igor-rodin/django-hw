from django.shortcuts import render, get_object_or_404
from django.http import HttpRequest
from .models import Author, Article

# Create your views here.


def author_articles(request: HttpRequest, auth_pk: int):
    author = get_object_or_404(Author, pk=auth_pk)
    articles = author.articles.all()
    context = {
        "title": "Статьи",
        "caption": "Все статьи",
        "author": author,
        "articles": articles,
    }
    return render(request, template_name="blog/articles.html", context=context)


def article_detail(request: HttpRequest, id: int):
    post = get_object_or_404(Article, pk=id)
    comments = post.comments.all()
    context = {
        "title": "Статья",
        "caption": "Статья",
        "post": post,
        "comments": comments,
    }
    return render(request, template_name="blog/article.html", context=context)
