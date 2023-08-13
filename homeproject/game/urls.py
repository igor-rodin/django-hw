from django.urls import path
from . import views

app_name = "game"

urlpatterns = [
    path("coin/<int:count>/", views.coin, name="coin"),
    path("dice/<int:count>/", views.dice, name="dice"),
    path("lucky/<int:count>/", views.lucky, name="lucky"),
    path("stat/", views.get_stat, name="get_stat"),
    path("", views.choose_game_form, name="choose_game"),
]
