from decimal import Decimal
from functools import cached_property, reduce
from django.db import models
from django.utils import dateformat


# Create your models here.
class Customer(models.Model):
    name = models.CharField(max_length=128, verbose_name="Имя клиента")
    email = models.EmailField(
        unique=True, db_index=True, verbose_name="Электронная почта клиента"
    )
    phone = models.CharField(max_length=12, verbose_name="Номер телефона клиента")
    address = models.TextField(verbose_name="Адрес клиента")
    created = models.DateTimeField(
        auto_now_add=True, verbose_name="Дата регистрации клиента"
    )

    def __str__(self):
        return f"Name: {self.name}, Email: {self.email}, Registered: {dateformat.format(self.created, 'd-m-Y H:i:s')}"


class Product(models.Model):
    title = models.CharField(
        max_length=128, db_index=True, verbose_name="Название товара"
    )
    description = models.TextField(
        blank=True, null=True, verbose_name="Описание товара"
    )
    price = models.DecimalField(
        max_digits=8, decimal_places=2, verbose_name="Цена товара"
    )
    # quantity = models.PositiveIntegerField(verbose_name="Количество товара")
    created = models.DateTimeField(
        auto_now_add=True, verbose_name="Дата добавления товара"
    )

    def __str__(self):
        return f"Name: {self.title}, Added: {dateformat.format(self.created, 'd-m-Y H:i:s')}"


class Order(models.Model):
    customer = models.ForeignKey(
        Customer, on_delete=models.CASCADE, related_name="orders", verbose_name="Клиент"
    )
    # products = models.ManyToManyField(
    #     Product,
    #     through="OrderLine",
    #     related_name="products",
    #     verbose_name="Товары в заказе",
    # )

    created = models.DateTimeField(
        auto_now_add=True, verbose_name="Дата оформления заказа"
    )

    def __str__(self):
        return f"Customer: {self.customer.name},  Created: {dateformat.format(self.created, 'd-m-Y H:i:s')}"

    @cached_property
    def total_price(self):
        res = Decimal(0)
        order_lines = OrderLine.objects.filter(order=self)
        for product in order_lines:
            res += product.product.price * product.quantity
        return res

    class Meta:
        ordering: ["-created"]
        indexes: models.Index(fields=["-created"])


class OrderLine(models.Model):
    order = models.ForeignKey(
        Order, on_delete=models.PROTECT, related_name="order", verbose_name="Заказ"
    )
    product = models.ForeignKey(
        Product,
        on_delete=models.PROTECT,
        related_name="product",
        verbose_name="Товар в заказе",
    )
    quantity = models.PositiveIntegerField(verbose_name="Количество товара в заказе")

    def __str__(self):
        return f"{self.product.title} - {self.quantity}"
