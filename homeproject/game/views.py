from django.shortcuts import render
from django.http import HttpResponse, HttpRequest
import random
import logging
from .models import Coin

logger = logging.getLogger(__name__)


# Create your views here.
def coin(request: HttpRequest, count: int):
    tries = []
    for _ in range(count):
        coin = Coin(coin_side=random.choice(Coin.Side.labels))
        coin.save()
        tries.append(coin)

    context = {"title": "Coin", "caption": "Бросание монеты", "tries": tries}

    logger.info(f"Run coin: {coin}")
    return render(request, template_name="game/game.html", context=context)


def dice(request: HttpRequest, count: int):
    tries = [random.randint(1, 6) for _ in range(count)]
    context = {"title": "Dice", "caption": "Бросание кости", "tries": tries}
    return render(request, template_name="game/game.html", context=context)


def lucky(request: HttpRequest, count: int):
    tries = [random.randint(1, 100) for _ in range(count)]
    context = {
        "title": "Lucky",
        "caption": "Случайное число от 1 до 1000",
        "tries": tries,
    }
    return render(request, template_name="game/game.html", context=context)
