from django.contrib import admin
from .models import Product, Order, OrderLine, Customer


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("title", "price", "description")


@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ("name", "email", "phone")


@admin.register(Order)
class OtrderAdmin(admin.ModelAdmin):
    list_display = ("customer", "created")


@admin.register(OrderLine)
class OtrderLineAdmin(admin.ModelAdmin):
    list_display = ("order", "product", "quantity")
