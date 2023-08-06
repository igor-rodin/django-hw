from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpRequest
import random
import logging
from .models import Coin
from .forms import GameForm

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


def choose_game_form(request: HttpRequest):
    if request.method == "POST":
        form = GameForm(request.POST)
        if form.is_valid():
            game_type = form.cleaned_data.get("game")
            n_attemts = form.cleaned_data.get("n_attempts")
            print(f"{game_type=}")
            match game_type:
                case "C":
                    return redirect("game:coin", count=n_attemts)
                case "D":
                    return redirect("game:dice", count=n_attemts)
                case "RN":
                    return redirect("game:lucky", count=n_attemts)
    else:
        form = GameForm()
    return render(
        request=request,
        template_name="game/choose_game_form.html",
        context={"form": form},
    )
