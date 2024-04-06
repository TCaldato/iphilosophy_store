from django import forms
from .models import Order

class OrderForm(forms.ModelForm):
    """
    Form for handling order information.
    """

    class Meta:
        """
        Meta class for defining form metadata.
        """
        model = Order
        fields = ('full_name', 'email', 'phone_number',
                  'street_address1', 'street_address2',
                  'town_or_city', 'postcode', 'country',
                  'county',)

    def __init__(self, *args, **kwargs):
        """
        Customize form initialization:
        - Add placeholders and classes
        - Remove auto-generated labels
        - Set autofocus on the first field
        """
        super().__init__(*args, **kwargs)
        
        # Define placeholders for form fields
        placeholders = {
            'full_name': 'Full Name',
            'email': 'Email Address',
            'phone_number': 'Phone Number',
            'country': 'Country',
            'postcode': 'Postal Code',
            'town_or_city': 'Town or City',
            'street_address1': 'Street Address 1',
            'street_address2': 'Street Address 2',
            'county': 'County',
        }

        # Set autofocus on the first field
        self.fields['full_name'].widget.attrs['autofocus'] = True
        
        # Loop through form fields to customize attributes
        for field in self.fields:
            placeholder = f'{placeholders[field]} *' if self.fields[field].required else placeholders[field]
            self.fields[field].widget.attrs['placeholder'] = placeholder
            self.fields[field].widget.attrs['class'] = 'stripe-style-input'
            self.fields[field].label = False
