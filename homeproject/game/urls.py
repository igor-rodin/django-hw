from django.urls import path
from . import views

app_name = "game"

urlpatterns = [
    path("coin/", views.coin, name="coin"),
    path("dice/", views.dice, name="dice"),
    path("lucky/", views.lucky, name="lucky"),
]
