from django.shortcuts import render
from django.http import HttpResponse, HttpRequest
import random
import logging
from .models import Coin

logger = logging.getLogger(__name__)


# Create your views here.
def coin(request: HttpRequest):
    coin = Coin(coin_side=random.choice(Coin.Side.labels))
    coin.save()
    logger.info("coin running...")
    return HttpResponse(f"<h2>{coin}</h2>")


def dice(request: HttpRequest):
    dice = random.randint(1, 6)
    return HttpResponse(f"<h2>{dice}</h2>")


def lucky(request: HttpRequest):
    lucky = random.randint(1, 100)
    return HttpResponse(f"<h2>{lucky}</h2>")
