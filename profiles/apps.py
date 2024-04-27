from django.apps import AppConfig


class ProfilesConfig(AppConfig):
    """
    This AppConfig class is used to configure
    some of the attributes of the 'profiles'
    application
    """

    default_auto_field = "django.db.models.BigAutoField"
    name = "profiles"
