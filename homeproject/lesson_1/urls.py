from django.urls import path
from . import views

app_name = "lesson_1"

urlpatterns = [
    path("", views.index, name="index"),
    path("about/", views.about, name="about"),
    path("test/", views.hello, name="hello"),
]
