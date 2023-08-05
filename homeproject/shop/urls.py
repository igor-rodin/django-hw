from django.urls import path
from . import views

app_name = "shop"

urlpatterns = [
    path(
        "",
        views.CustomersView.as_view(),
        name="customers",
    ),
    path(
        "customers/<int:cust_id>/orders/",
        views.customer_orders,
        name="customer_orders",
    ),
    path(
        "customers/<int:cust_id>/products/<slug:period>/",
        views.ProductsView.as_view(),
        name="customer_products",
    ),
]
