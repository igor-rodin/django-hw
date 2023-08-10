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

    class Meta:
        verbose_name = "Клиент"
        verbose_name_plural = "Клиенты"


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
    image = models.ImageField(upload_to="products/", null=True, default=None)
    created = models.DateTimeField(
        auto_now_add=True, verbose_name="Дата добавления товара"
    )

    def __str__(self):
        return f"Name: {self.title}, Added: {dateformat.format(self.created, 'd-m-Y H:i:s')}"

    class Meta:
        verbose_name = "Товар"
        verbose_name_plural = "Товары"


class Order(models.Model):
    customer = models.ForeignKey(
        Customer, on_delete=models.CASCADE, related_name="orders", verbose_name="Клиент"
    )

    created = models.DateTimeField(
        auto_now_add=True, verbose_name="Дата оформления заказа"
    )

    def __str__(self):
        return f"Customer: {self.customer.name},  Created: {dateformat.format(self.created, 'd-m-Y H:i:s')}"

    @cached_property
    def total_price(self) -> Decimal:
        res = Decimal(0)
        order_lines = OrderLine.objects.filter(order=self)
        for product in order_lines:
            res += product.product.price * product.quantity
        return res

    class Meta:
        verbose_name = "Заказ"
        verbose_name_plural = "Заказы"
        ordering: ["-created"]
        indexes: models.Index(fields=["-created"])


class OrderLine(models.Model):
    order = models.ForeignKey(
        Order,
        on_delete=models.PROTECT,
        related_name="order_lines",
        verbose_name="Заказ",
    )
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        related_name="product",
        verbose_name="Товар в заказе",
    )
    quantity = models.PositiveIntegerField(verbose_name="Количество товара в заказе")

    @cached_property
    def total_price(self) -> Decimal:
        return self.product.price * self.quantity

    def __str__(self):
        return f"{self.product.title}-{self.quantity}"

    class Meta:
        verbose_name = "Строка заказа"
        verbose_name_plural = "Состав заказа"
        ordering = ["-pk"]
