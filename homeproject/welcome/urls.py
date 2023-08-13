from django.urls import path
from . import views

app_name = "welcome"
verbose_name = "Главная"

urlpatterns = [path("", views.index, name="index")]
