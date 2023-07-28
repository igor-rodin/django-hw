from collections import defaultdict
from django.db import models
from django.utils import timezone


# Create your models here.
class Coin(models.Model):
    class Side(models.TextChoices):
        HEADS = "H", "Heads"
        TAILS = "T", "Tails"

    coin_side = models.CharField(max_length=5, choices=Side.choices)
    time_throw = models.DateTimeField(default=timezone.now)

    def __str__(self) -> str:
        return f"{self.coin_side}:{self.time_throw}"

    @staticmethod
    def get_stat(n_last: int) -> dict[str, int]:
        all_throws = Coin.objects.all()[:n_last]
        stats = defaultdict(int)
        for throw in all_throws:
            stats[throw.coin_side] += 1
        return stats

    class Meta:
        ordering = ["-time_throw"]
