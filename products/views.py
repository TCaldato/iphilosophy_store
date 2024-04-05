from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from django.db.models.functions import Lower

from .models import Product, Category

def all_products(request):
    """ A view to show all products, including sorting and search queries """

    # Get all products initially
    products = Product.objects.all()
    query = None 
    categories = None
    sort = None  
    direction = None  

    # Check if there are any GET parameters in the request
    if request.GET:
        # Check if 'sort' parameter is in the GET request
        if 'sort' in request.GET:
            sort = request.GET['sort']
            sortkey = sort
            
            # Check if sorting by name
            if sortkey == 'name':
                sortkey = 'lower_name'
                products = products.annotate(lower_name=Lower('name'))
            
            # Check if sorting by category
            if sortkey == 'category':
                sortkey = 'category__name'
            
            # Check if 'direction' parameter is in the GET request
            if 'direction' in request.GET:
                direction = request.GET['direction']
                
                # Check if direction is descending
                if direction == 'desc':
                    sortkey = f'-{sortkey}'
                
            products = products.order_by(sortkey)
        
        # Check if 'category' parameter is in the GET request
        if 'category' in request.GET:
            categories = request.GET['category'].split(',')
            products = products.filter(category__name__in=categories)
            categories = Category.objects.filter(name__in=categories)

        # Check if 'q' parameter is in the GET request
        if 'q' in request.GET:
            query = request.GET['q']
            
            # Check if query is empty
            if not query:
                # If query is empty, display error message and redirect to products page
                messages.error(request, "You didn't enter any search criteria!")
                return redirect(reverse('products'))
            
            # Define search criteria
            queries = Q(name__icontains=query) | Q(description__icontains=query)
            products = products.filter(queries)

    current_sorting = f'{sort}_{direction}'
    
    context = {
        'products': products,
        'search_term': query,
        'current_categories': categories,
        'current_sorting': current_sorting,
    }

    return render(request, 'products/products.html', context)


def product_detail(request, product_id):
    """ A view to show individual product details """

    product = get_object_or_404(Product, pk=product_id)

    context = {
        'product': product,
    }

    return render(request, 'products/product_detail.html', context)