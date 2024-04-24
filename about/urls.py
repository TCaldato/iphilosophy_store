from . import views
from django.urls import path

urlpatterns = [
    # URL pattern for the About Me page
    path("", views.about_me, name="about"),
]
