
from django import forms
from .widgets import CustomClearableFileInput
from .models import Product, Category


class ProductForm(forms.ModelForm):
    """
    A form for creating and updating Product instances.
    """

    class Meta:
        """
        Includes all fields from the Product model in the form.
        """
        model = Product
        fields = '__all__'

    image = forms.ImageField(label='Image', required=False, widget=CustomClearableFileInput)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # pylint: disable=no-member #Inline Pylint Disable Comments
        categories = Category.objects.all()
        friendly_names = [(c.id, c.get_friendly_name()) for c in categories] # Create a list of tuples for dropdown choices

        self.fields['category'].choices = friendly_names
        for _, field in self.fields.items():
            field.widget.attrs['class'] = 'border-black rounded-0'
