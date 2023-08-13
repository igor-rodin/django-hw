import logging
from typing import Any, Dict
from datetime import date, timedelta
from django.urls import reverse_lazy
from django.http import HttpRequest, Http404
from django.db.models import Sum
from django.db.models.query import QuerySet
from django.shortcuts import render, get_list_or_404, redirect
from django.views.generic import ListView, DetailView
from django.views.generic.edit import UpdateView, DeleteView
from .models import OrderLine, Order, Customer, Product
from .forms import ProductForm


logger = logging.getLogger(__name__)

DAYS_IN_WEEK = 7
DAYS_IN_MONTH = 30
DAYS_IN_YEAR = 365


def get_period(period: str) -> (list[date], str):
    end_date = date.today() + timedelta(days=1)
    end_date = end_date + timedelta(days=1)
    verbose_name = None
    match period:
        case "week":
            start_date = end_date - timedelta(days=DAYS_IN_WEEK)
            verbose_name = "неделю"
        case "month":
            start_date = end_date - timedelta(days=DAYS_IN_MONTH)
            verbose_name = "месяц"
        case "year":
            start_date = end_date - timedelta(days=DAYS_IN_YEAR)
            verbose_name = "год"
        case _:
            return None
    return ([start_date, end_date], verbose_name)


def customer_orders(request: HttpRequest, cust_id: int):
    orders = get_list_or_404(Order.objects.order_by("-created"), customer__pk=cust_id)
    cust_order = orders[0].customer.name
    context = {
        "customer": cust_order,
        "orders": orders,
        "title": "Заказы",
    }
    return render(request=request, template_name="shop/orders.html", context=context)


class ProductsView(ListView):
    model = OrderLine
    template_name = "shop/products.html"
    context_object_name = "products"
    allow_empty = True

    def get_queryset(self) -> QuerySet[Any]:
        period = get_period(self.kwargs["period"])
        if period is None:
            raise Http404("Страница не найдена")
        date_period, _ = period
        return (
            OrderLine.objects.filter(
                order__customer__pk=self.kwargs["cust_id"],
                order__created__range=date_period,
            )
            .values("product__title")
            .annotate(total_quantity=Sum("quantity"))
            .order_by("-total_quantity")
        )

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)
        _, name = get_period(self.kwargs["period"])
        customer = Customer.objects.filter(pk=self.kwargs["cust_id"]).first()
        context["title"] = f"Заказано за {name}"
        context["customer"] = customer
        return context


class CustomersView(ListView):
    model = Customer
    template_name = "shop/customers.html"
    context_object_name = "customers"
    extra_context = {"title": "Клиенты"}


def add_product(request: HttpRequest):
    if request.method == "POST":
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = Product.objects.create(**form.cleaned_data)
            logger.debug(f"Product added: {product=}")
            return redirect("shop:all_products")

    else:
        form = ProductForm()
    context = {"form": form, "caption": "Новый товар", "button_caption": "Добавить"}
    return render(request, template_name="shop/product_form.html", context=context)


class ProductUpdateView(UpdateView):
    form_class = ProductForm
    model = Product
    template_name = "shop/product_form.html"
    extra_context = {"caption": "Обновить товар", "button_caption": "Сохранить"}
    success_url = reverse_lazy("shop:all_products")
    context_object_name = "product"


class CatalogVew(ListView):
    model = Product
    template_name = "shop/catalog.html"
    context_object_name = "catalog"
    extra_context = {"title": "Каталог товаров"}


class ProductDeleteVew(DeleteView):
    model = Product
    template_name = "shop/product_confirm_delete.html"
    context_object_name = "product"
    success_url = reverse_lazy("shop:all_products")


class ProductVew(DetailView):
    model = Product
    template_name = "shop/product_detail.html"
    context_object_name = "product"
