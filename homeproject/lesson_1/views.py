from django.shortcuts import render
from django.http import HttpResponse, HttpRequest
import logging

logger = logging.getLogger(__name__)


# Create your views here.
def hello(request: HttpRequest):
    logger.info("hello running...")
    return HttpResponse("<h1>Hello, World!</h1>")
