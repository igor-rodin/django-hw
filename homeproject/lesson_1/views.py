from django.shortcuts import render
from django.http import HttpResponse, HttpRequest
import logging

logger = logging.getLogger(__name__)


# Create your views here.
def hello(request: HttpRequest):
    logger.info("hello running...")
    return HttpResponse("<h1>Hello, World!</h1>")


def index(requset: HttpRequest):
    context = {
        "title": "Главная",
        "caption": "Homeproject - Powered by Django",
        "content": "Домашний проект на Django. Позже здесь будет больше информации",
    }
    logger.info(
        f"Acces to main page from {requset.META.get('REMOTE_ADDR')}, user agent: {requset.META.get('HTTP_USER_AGENT')}"
    )
    return render(requset, template_name="lesson_1/index.html", context=context)


def about(requset: HttpRequest):
    context = {
        "title": "Обо мне",
        "content": "Программа: Web разработка на Python (Django)",
    }

    logger.info(
        f"Acces to about page from {requset.META.get('REMOTE_ADDR')}, user agent: {requset.META.get('HTTP_USER_AGENT')}"
    )
    return render(requset, template_name="lesson_1/about.html", context=context)
