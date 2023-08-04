from typing import Any
from django.http import HttpRequest
from django.db.models.query import QuerySet
from django.shortcuts import render, get_object_or_404, get_list_or_404
from django.views.generic import ListView
from .models import OrderLine, Order


# class OrdersView(ListView):
#     model = OrderLine
#     template_name = "shop/orders.html"
#     context_object_name = "orders"


#     def get_queryset(self) -> QuerySet[Any]:
#         return OrderLine.objects.filter(order__customer__pk=self.kwargs["cust_id"])
def customer_orders(request: HttpRequest, cust_id: int):
    # order = Order

    order_lines = get_list_or_404(OrderLine, order__customer__pk=cust_id)
    print(order_lines)
    # order_lines = OrderLine.objects.filter(order__customer__pk=cust_id)
    cust_order = order_lines[0].order.customer.name
    print(cust_order)
    # cust_order = order_lines.order
    context = {"customer": cust_order, "order_lines": order_lines, "title": "Заказы"}
    return render(request=request, template_name="shop/orders.html", context=context)
