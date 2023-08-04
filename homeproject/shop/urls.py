from django.urls import path
from . import views

app_name = "shop"

urlpatterns = [
    path(
        "customers/<int:cust_id>/orders/",
        views.customer_orders,
        name="customer_orders",
    ),
]
