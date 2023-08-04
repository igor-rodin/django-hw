from django.shortcuts import render, get_object_or_404
from django.http import HttpRequest
from .models import Author, Article
from .forms import AuthorForms
import logging

logger = logging.getLogger(__name__)


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


def add_author(request: HttpRequest):
    if request.method == "POST":
        form = AuthorForms(request.POST)
        if form.is_valid():
            name = form.cleaned_data.get("name")
            surname = form.cleaned_data.get("surname")
            email = form.cleaned_data.get("email")
            biography = form.cleaned_data.get("biography")
            birthday = form.cleaned_data.get("birthday")
            logger.info(f"Get {name} {surname} {email} {biography} {birthday}")
    else:
        form = AuthorForms()
    return render(
        request=request, template_name="blog/author_form.html", context={"form": form}
    )
