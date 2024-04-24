from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import About, CollaborateRequest


@admin.register(About)
class AboutAdmin(SummernoteModelAdmin):
    """Admin interface for the About model."""

    summernote_fields = ("content",)
    # Use Summernote editor for the 'content' field.


@admin.register(CollaborateRequest)
class CollaborateRequestAdmin(admin.ModelAdmin):
    """This class configures the admin view for
    CollaborateRequest models
    """

    # Display 'message' and 'read' status in the admin list.
    list_display = (
        "message",
        "read",
    )
