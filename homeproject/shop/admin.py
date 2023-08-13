from django.contrib import admin
from .models import Product, Order, OrderLine, Customer

admin.site.site_header = "Администрирование приложений курса Django"


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("title", "price", "description")
    list_filter = ("created",)
    ordering = ["-created"]
    search_fields = ["title", "description"]
    search_help_text = "Поиск по названию и описанию товара"
    fieldsets = [
        (None, {"classes": ["wide"], "fields": ["title", "price"]}),
        (
            "Характеристики",
            {"classes": ["collapse"], "fields": ["description", "image", "created"]},
        ),
    ]
    readonly_fields = ["created"]


@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ("name", "email", "phone")
    ordering = ["name"]
    search_fields = ["name", "email", "phone", "address"]
    search_help_text = "Поиск по данным клиента(имя, телефон, адрес, email)"
    fieldsets = [
        (
            None,
            {
                "classes": ["wide"],
                "fields": [
                    ("name", "created"),
                ],
            },
        ),
        (
            "Контакты",
            {"classes": ["collapse"], "fields": ["email", "phone", "address"]},
        ),
    ]
    readonly_fields = ["created"]


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ("view_customer_name", "view_total_price", "created")
    ordering = ["-created", "customer__name"]
    list_filter = ("created",)
    search_fields = ["customer__name", "customer__email"]
    search_help_text = "Поиск по данным заказа(имя, email клиента)"
    fields = ["customer", "view_customer_email", ("view_total_price", "created")]
    readonly_fields = ["view_total_price", "view_customer_email", "created"]

    @admin.display(description="Имя клиента")
    def view_customer_name(self, obj):
        return obj.customer.name

    @admin.display(
        description="Email клиента",
    )
    def view_customer_email(self, obj):
        return obj.customer.email

    @admin.display(description="Сумма заказа, руб")
    def view_total_price(self, obj):
        return obj.total_price


@admin.register(OrderLine)
class OrderLineAdmin(admin.ModelAdmin):
    list_display = ("order", "view_product_title", "quantity")
    list_filter = ("order__created", "order__customer__name")
    search_fields = ["order__customer__name", "product__title"]
    search_help_text = "Поиск по данным заказа(имя клиента, название товара)"

    @admin.display(description="Товар")
    def view_product_title(self, obj):
        return obj.product.title
