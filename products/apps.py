from django.apps import AppConfig


class ProductsConfig(AppConfig):
    """
    This AppConfig class is used to configure
    some of the attributes of the application
    """

    default_auto_field = "django.db.models.BigAutoField"
    name = "products"
