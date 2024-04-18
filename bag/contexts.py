from decimal import Decimal
from django.conf import settings
from django.shortcuts import get_object_or_404
from products.models import Product


def bag_contents(request):
    """
    Retrieve the contents of the shopping bag 
    from the session and calculate various totals.
    """

    bag_items = []
    total = 0
    product_count = 0
    bag = request.session.get("bag", {})

    # Loop through each item in the bag
    for item_id, quantity in bag.items():
        product = get_object_or_404(Product, pk=item_id)
        total += quantity * product.price
        product_count += quantity
        bag_items.append(
            {  # Append product details to the bag_items list
                "item_id": item_id,
                "quantity": quantity,
                "product": product,
            }
        )

    # Calculate delivery charges
    if total < settings.FREE_DELIVERY_THRESHOLD:
        delivery = total * Decimal(settings.STANDARD_DELIVERY_PERCENTAGE / 100)
        free_delivery_delta = settings.FREE_DELIVERY_THRESHOLD - total
    else:
        delivery = 0  # No delivery cost if total is above threshold
        free_delivery_delta = 0

    grand_total = delivery + total

    # Prepare the context dictionary to return
    context = {
        "bag_items": bag_items,
        "total": total,
        "product_count": product_count,
        "delivery": delivery,
        "free_delivery_delta": free_delivery_delta,
        "free_delivery_threshold": settings.FREE_DELIVERY_THRESHOLD,
        "grand_total": grand_total,
    }

    return context
