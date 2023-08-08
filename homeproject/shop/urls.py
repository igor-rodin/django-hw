from django.urls import path
from . import views

app_name = "shop"
verbose_name = "Магазин"


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
    path(
        "products/",
        views.CatalogVew.as_view(),
        name="all_products",
    ),
    path(
        "products/<int:pk>/",
        views.ProductVew.as_view(),
        name="product_detail",
    ),
    path(
        "products/add/",
        views.add_product,
        name="add_product",
    ),
    path(
        "products/update/<int:pk>/",
        views.ProductUpdateView.as_view(),
        name="update_product",
    ),
    path(
        "products/delete/<int:pk>/",
        views.ProductDeleteVew.as_view(),
        name="delete_product",
    ),
]
