from django import forms
from .widgets import CustomClearableFileInput
from .models import Product, Category, Review


class ProductForm(forms.ModelForm):
    """
    A form for creating and updating Product instances.
    """

    class Meta:
        """
        Includes all fields from the Product model in the form.
        """

        model = Product
        fields = "__all__"

    image = forms.ImageField(
        label="Image", required=False, widget=CustomClearableFileInput
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        categories = Category.objects.all()
        # Create a list of tuples for dropdown choices
        friendly_names = [(c.id, c.get_friendly_name()) for c in categories]

        self.fields["category"].choices = friendly_names
        for _, field in self.fields.items():
            field.widget.attrs["class"] = "border-black rounded-0"


class ReviewForm(forms.ModelForm):
    """This form allows users to create new review instances or update existing ones."""

    class Meta:
        """Defines metadata options for the ReviewForm class,"""

        model = Review
        fields = ("review_text", "rating")
