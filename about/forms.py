from .models import CollaborateRequest
from django import forms


class CollaborateForm(forms.ModelForm):
    """
    This form is tied directly to the CollaborateRequest
    model and allows users to submit their name, email,
    and a message through a web form.
    """

    class Meta:
        model = CollaborateRequest
        fields = ("name", "email", "message")
