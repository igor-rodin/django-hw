from django.contrib import admin
from .models import Product, Order, OrderLine, Customer


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("title", "price", "description")
    # list_filter = ()


@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ("name", "email", "phone")
    ordering = ["name"]
    search_fields = ["name", "email", "phone", "address"]
    search_help_text = "Поиск по данным клиента(имя, телефон, адрес, email)"
    fieldsets = [
        (None, {"classes": ["wide"], "fields": ["name", "created"]}),
        (
            "Контакты",
            {"classes": ["collapse"], "fields": ["email", "phone", "address"]},
        ),
    ]
    readonly_fields = ["created"]


@admin.register(Order)
class OtrderAdmin(admin.ModelAdmin):
    list_display = ("customer", "created")


@admin.register(OrderLine)
class OtrderLineAdmin(admin.ModelAdmin):
    list_display = ("order", "product", "quantity")
