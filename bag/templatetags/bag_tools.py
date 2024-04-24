from django import template


register = template.Library()


@register.filter(name="calc_subtotal")
def calc_subtotal(price, quantity):
    """
    Calculate the subtotal for a given quantity of items at a specific price.
    """
    return price * quantity
