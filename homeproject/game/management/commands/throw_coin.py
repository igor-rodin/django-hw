from typing import Any, Optional
from django.core.management.base import BaseCommand
from game.models import Coin
from random import choice


class Command(BaseCommand):
    help = "Throw coin"

    def handle(self, *args: Any, **options: Any) -> str | None:
        sides = Coin.Side.labels
        coin = Coin(coin_side=choice(sides))
        coin.save()
        self.stdout.write(f"{coin}")
