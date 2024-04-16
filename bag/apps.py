from django.apps import AppConfig # Module imports the AppConfig class from Django's apps module.


class BagConfig(AppConfig):
    """
    Configuration class for the 'bag' application.
    """
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'bag'
