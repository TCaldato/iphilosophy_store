from django.contrib import admin
from .models import Product, Category


class ProductAdmin(admin.ModelAdmin):
    """
    This class customizes the appearance and
    functionality of the Product model within the
    Django admin site.
    """

    list_display = (
        "sku",
        "name",
        "author",
        "category",
        "price",
        "rating",
        "image",
    )

    ordering = ("sku",)


class CategoryAdmin(admin.ModelAdmin):
    """
    This class customizes how categories are
    displayed within the Django admin site.
    """

    list_display = (
        "friendly_name",
        "name",
    )


admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
