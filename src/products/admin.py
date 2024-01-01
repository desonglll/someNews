from django.contrib import admin

from .models import Product

Product._meta.verbose_name = "product"
Product._meta.verbose_name_plural = "products"


class ProductAdmin(admin.ModelAdmin):
    list_display = ("id", 'product_name', "name", 'price', "operation", "quantity", "buy_date")  # 在列表中显示的字段
    list_display_links = ("id", 'product_name', "name", 'price', 'operation', 'quantity', 'buy_date')

    pass


admin.site.register(Product, ProductAdmin)
