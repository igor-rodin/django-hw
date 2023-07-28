from typing import Any
from django.core.management.base import BaseCommand, CommandParser
from game.models import Coin


class Command(BaseCommand):
    help = "Get throws statistic"

    def add_arguments(self, parser: CommandParser) -> None:
        parser.add_argument("n_last", type=int, help="Last throws")

    def handle(self, *args: Any, **options: Any) -> str | None:
        lasts = options.get("n_last")
        stat = Coin.get_stat(n_last=lasts)
        self.stdout.write(f"{stat}")
