from typing import Any
from django.core.management.base import BaseCommand, CommandParser
from game.models import Coin


class Command(BaseCommand):
    help = "All coin throws"

    def handle(self, *args: Any, **options: Any) -> str | None:
        throws = Coin.objects.all()
        self.stdout.write(f"{throws}\n")
        self.stdout.write(f"Total: {throws.count()}")
