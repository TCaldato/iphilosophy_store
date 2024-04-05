from django.shortcuts import render, redirect, reverse
from django.http import HttpResponse
from django.contrib import messages

from products.models import Product

# Create your views here.

def view_bag(request):
    """ A view that renders the bag contents page """
    return render(request, 'bag/bag.html')

def add_to_bag(request, item_id):
    """ Add a quantity of the specified product to the shopping bag """

    if request.method == 'POST':
        product = Product.objects.get(pk=item_id)
        quantity = int(request.POST.get('quantity', 1))
        redirect_url = request.POST.get('redirect_url')

        bag = request.session.get('bag', {})
        bag[item_id] = bag.get(item_id, 0) + quantity

        request.session['bag'] = bag

        messages.success(request, f'Added {product.name} to your bag')
        return redirect(redirect_url)

    return redirect(reverse('view_bag'))

def adjust_bag(request, item_id):
    """Adjust the quantity of the specified product to the specified amount"""

    if request.method == 'POST':
        quantity = int(request.POST.get('quantity', 0))

        bag = request.session.get('bag', {})
        if quantity > 0:
            bag[item_id] = quantity
        else:
            bag.pop(item_id, None)

        request.session['bag'] = bag

    return redirect(reverse('view_bag'))

def remove_from_bag(request, item_id):
    """Remove the item from the shopping bag"""

    if request.method == 'POST':
        bag = request.session.get('bag', {})
        bag.pop(item_id, None)
        request.session['bag'] = bag
        return HttpResponse(status=200)

    return HttpResponse(status=400)
