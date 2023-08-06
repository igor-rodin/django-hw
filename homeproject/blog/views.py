import logging
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpRequest
from django.db.models import F
from .models import Author, Article, Comment
from .forms import AuthorForm, ArticleForm, CommentForm

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
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.cleaned_data.get("comment")
            author = form.cleaned_data.get("author")
            article = get_object_or_404(Article, pk=id)
            logger.info(f"Add comment: {comment}  {author}")
            comment = Comment(comment=comment, author=author, article=article)
            comment.save()
            post.n_views = F("n_views") - 1
            post.save()
            post.refresh_from_db()
            return redirect("blog:article_detail", id=id)
    else:
        form = CommentForm()
        post.n_views = F("n_views") + 1
        post.save()
        post.refresh_from_db()
        context["form"] = form

    return render(request, template_name="blog/article.html", context=context)


def add_author(request: HttpRequest):
    if request.method == "POST":
        form = AuthorForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data.get("name")
            surname = form.cleaned_data.get("surname")
            email = form.cleaned_data.get("email")
            biography = form.cleaned_data.get("biography")
            birthday = form.cleaned_data.get("birthday")
            Author.objects.create(
                name=name,
                surname=surname,
                email=email,
                biography=biography,
                birtday=birthday,
            )
            logger.info(f"Add author: {name} {surname} {email} {biography} {birthday}")
    else:
        form = AuthorForm()
    return render(
        request=request, template_name="blog/author_form.html", context={"form": form}
    )


def add_article(request: HttpRequest):
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data.get("title")
            content = form.cleaned_data.get("content")
            category = form.cleaned_data.get("category")
            author = form.cleaned_data.get("author")
            logger.info(f"Add aarticle: {title} {category} {author}")
            article = Article(
                title=title,
                content=content,
                category=category,
                author=author,
            )
            article.save()
            return redirect("blog:article_detail", id=article.pk)
    else:
        form = CommentForm()
    return render(
        request=request, template_name="blog/article_form.html", context={"form": form}
    )
