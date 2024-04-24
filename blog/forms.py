from django import forms
from .models import Comment


class CommentForm(forms.ModelForm):
    """
    Meta class for the CommentForm, specifies metadata options.
    """

    class Meta:
        model = Comment
        fields = ("body",)
