from django.shortcuts import render
from django.http import HttpResponse, HttpRequest
import logging

logger = logging.getLogger(__name__)


# Create your views here.
def hello(request: HttpRequest):
    logger.info("hello running...")
    return HttpResponse("<h1>Hello, World!</h1>")


def index(requset: HttpRequest):
    main_page = """
    <!doctype html>
        <html lang="ru">

        <head>
            <meta charset="utf-8">
            <meta name="viewport" content="width=device-width, initial-scale=1">
            <title>Homeproject - Главная</title>
            <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet"
                integrity="sha384-9ndCyUaIbzAi2FUVXJi0CjmCapSmO7SnpJef0486qhLnuZ2cdeRhO02iuK6FUUVM" crossorigin="anonymous">
        </head>

        <body>
            <div class="container-fluid">
                <nav class="navbar navbar-expand-lg bg-body-tertiary">
                    <div class="container">
                        <a class="navbar-brand" href="#">HomeProject</a>
                        <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNavAltMarkup" aria-controls="navbarNavAltMarkup" aria-expanded="false" aria-label="Toggle navigation">
                        <span class="navbar-toggler-icon"></span>
                        </button>
                        <div class="collapse navbar-collapse" id="navbarNavAltMarkup">
                            <div class="navbar-nav">
                                <a class="nav-link active" aria-current="page">Главная</a>
                                <a class="nav-link" href="http://127.0.0.1:8000/about">О нас</a>
                            </div>
                        </div>
                    </div>
                </nav>    
            </div>
            
            <div class="container m-lg-auto">
                <h1 class="h1 m-5 text-end">Homeproject - Powered by Django</h1>
                <div class="row col-12" >
                    <p class="lead fs-1 fc text-success">Домашний проект на Django. Позже здесь будет больше информации</p>
                </div>
            </div>

            <footer class="footer  mt-auto bg-light py-3 fixed-bottom">
                <div class="container">
                    <span class="text-muted">&copy; 2023 HomeProject</span>
                </div>
            </footer>

            <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/js/bootstrap.bundle.min.js"
                integrity="sha384-geWF76RCwLtnZ8qwWowPQNguL3RmwHVBC9FhGdlKrxdiJJigb/j/68SIy3Te4Bkz"
                crossorigin="anonymous"></script>
        </body>

        </html>
    """
    logger.info(
        f"Acces to main page from {requset.META.get('REMOTE_ADDR')}, user agent: {requset.META.get('HTTP_USER_AGENT')}"
    )
    return HttpResponse(main_page)


def about(requset: HttpRequest):
    about_page = """
    <!doctype html>
        <html lang="ru">

        <head>
            <meta charset="utf-8">
            <meta name="viewport" content="width=device-width, initial-scale=1">
            <title>Homeproject - О нас</title>
            <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet"
                integrity="sha384-9ndCyUaIbzAi2FUVXJi0CjmCapSmO7SnpJef0486qhLnuZ2cdeRhO02iuK6FUUVM" crossorigin="anonymous">
        </head>

        <body>
            <div class="container-fluid">
                <nav class="navbar navbar-expand-lg bg-body-tertiary">
                    <div class="container">
                        <a class="navbar-brand" href="#">HomeProject</a>
                        <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNavAltMarkup" aria-controls="navbarNavAltMarkup" aria-expanded="false" aria-label="Toggle navigation">
                        <span class="navbar-toggler-icon"></span>
                        </button>
                        <div class="collapse navbar-collapse" id="navbarNavAltMarkup">
                        <div class="navbar-nav">
                            <a class="nav-link" aria-current="page" href="http://127.0.0.1:8000/">Главная</a>
                            <a class="nav-link active" aria-current="page">О нас</a>
                        </div>
                        </div>
                    </div>
                </nav>    
            </div>
            
            <div class="container m-lg-auto text-center">
                <h1 class="h1 m-5">О нас</h1>
                <div class="row col-12" >
                    <p class="lead fs-2 fc text-primary-emphasis">Программа: Web разработка на Python (Django)</p>
                </div>
            </div>
            
            <footer class="footer  mt-auto bg-light py-3 fixed-bottom">
                <div class="container">
                    <span class="text-muted">&copy; 2023 HomeProject</span>
                </div>
            </footer>

            <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/js/bootstrap.bundle.min.js"
                integrity="sha384-geWF76RCwLtnZ8qwWowPQNguL3RmwHVBC9FhGdlKrxdiJJigb/j/68SIy3Te4Bkz"
                crossorigin="anonymous"></script>
        </body>

        </html>
    """
    logger.info(
        f"Acces to about page from {requset.META.get('REMOTE_ADDR')}, user agent: {requset.META.get('HTTP_USER_AGENT')}"
    )
    return HttpResponse(about_page)
