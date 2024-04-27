from django.shortcuts import render, redirect, get_object_or_404, reverse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.db.models.functions import Lower
from django.http import HttpResponseRedirect

from .models import Product, Category, Review, Wishlist
from .forms import ProductForm, ReviewForm


def all_products(request):
    """A view to show all products, including sorting and search queries"""
    products = Product.objects.all()
    query = None
    categories = None
    sort = None
    direction = None

    # Handling GET request with parameters for sorting and filtering
    if request.GET:
        if "sort" in request.GET:
            sortkey = request.GET["sort"]
            sort = sortkey
            if sortkey == "name":
                sortkey = "lower_name"
                products = products.annotate(lower_name=Lower("name"))
            if sortkey == "category":
                sortkey = "category__name"
            if "direction" in request.GET:
                direction = request.GET["direction"]
                if direction == "desc":
                    sortkey = f"-{sortkey}"
            products = products.order_by(sortkey)

        # Filtering products by category
        if "category" in request.GET:
            categories = request.GET["category"].split(",")
            products = products.filter(category__name__in=categories)
            categories = Category.objects.filter(name__in=categories)

        # Search functionality
        if "q" in request.GET:
            query = request.GET["q"]
            if not query:
                messages.error(request, "You didn't enter any search criteria!")
                return redirect(reverse("products"))

            queries = Q(name__icontains=query) | Q(description__icontains=query)
            products = products.filter(queries)

    current_sorting = f"{sort}_{direction}"

    context = {
        "products": products,
        "search_term": query,
        "current_categories": categories,
        "current_sorting": current_sorting,
    }

    return render(request, "products/products.html", context)


def product_detail(request, product_id):
    """A view to show individual product details"""

    product = get_object_or_404(
        Product, pk=product_id
    )  # Retrieve product or show 404 error

    context = {
        "product": product,
    }

    return render(request, "products/product_detail.html", context)


@login_required
def add_product(request):
    """View to add a new product to the store. Accessible only by superusers."""
    if not request.user.is_superuser:
        messages.error(request, "Sorry, only store owners can do that.")
        return redirect(reverse("home"))

    if request.method == "POST":
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save()
            messages.success(request, "Successfully added product!")
            return redirect(reverse("product_detail", args=[product.id]))
        else:
            messages.error(
                request, "Failed to add product. Please ensure the form is valid."
            )
    else:
        form = ProductForm()

    template = "products/add_product.html"
    context = {
        "form": form,
    }

    return render(request, template, context)


@login_required
def edit_product(request, product_id):
    """View to edit an existing product. Accessible only by superusers."""
    if not request.user.is_superuser:
        messages.error(request, "Sorry, only store owners can do that.")
        return redirect(reverse("home"))

    product = get_object_or_404(Product, pk=product_id)
    if request.method == "POST":
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            messages.success(request, "Successfully updated product!")
            return redirect(reverse("product_detail", args=[product.id]))
        else:
            messages.error(
                request, "Failed to update product. Please ensure the form is valid."
            )
    else:
        form = ProductForm(instance=product)
        messages.info(request, f"You are editing {product.name}")

    template = "products/edit_product.html"
    context = {
        "form": form,
        "product": product,
    }

    return render(request, template, context)


@login_required
def delete_product(request, product_id):
    """View to delete a product from the store. Accessible only by superusers."""
    if not request.user.is_superuser:
        messages.error(request, "Sorry, only store owners can do that.")
        return redirect(reverse("home"))

    product = get_object_or_404(Product, pk=product_id)
    product.delete()
    messages.success(request, "Product deleted!")
    return redirect(reverse("products"))


@login_required
def add_review(request, product_id):
    """
    Allow an authenticated user to add a review to a specific product.
    """
    product = get_object_or_404(Product, pk=product_id)
    if request.method == "POST":
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.product = product
            review.user = request.user
            review.save()
            messages.success(request, "Your review has been added!")
            return redirect("product_detail", product_id=product_id)
    else:
        form = ReviewForm()
    return render(
        request, "products/add_review.html", {"form": form, "product": product}
    )


@login_required
def edit_review(request, product_id, review_id):
    """
    View to edit reviews. Ensure that only the author of the review can edit it.
    """
    review = get_object_or_404(
        Review, pk=review_id, user=request.user, product_id=product_id
    )  # Ensure only the author can edit.

    if request.method == "POST":
        review_form = ReviewForm(request.POST, instance=review)
        if review_form.is_valid():
            review_form.save()
            messages.success(request, "Review updated successfully!")
            return redirect(
                "product_detail", product_id=product_id
            )  # Redirect to product detail page.
        else:
            messages.error(request, "Error updating review. Please check the form.")

    else:
        review_form = ReviewForm(instance=review)

    return render(
        request,
        "products/edit_review.html",
        {"form": review_form, "product_id": product_id},
    )


@login_required
def delete_review(request, product_id, review_id):
    """
    Allow an authenticated user to delete their own review of a product.
    """
    review = get_object_or_404(Review, id=review_id, user=request.user)
    if request.method == "POST":
        review.delete()
        messages.success(request, "Review deleted successfully!")
        return redirect("product_detail", product_id=product_id)
    else:
        messages.error(request, "Invalid method")
        return redirect("product_detail", product_id=product_id)


@login_required
def view_wishlist(request):
    """
    Display the user's wishlist.
    """
    wishlist, created = Wishlist.objects.get_or_create(user=request.user)
    return render(request, "products/wishlist.html", {"wishlist": wishlist})


@login_required
def add_to_wishlist(request, product_id):
    """
    Add a product to the user's wishlist. Redirects the user back to the page they
    were on, either the product detail page or a general product list page.
    """
    product = get_object_or_404(Product, id=product_id)
    wishlist, created = Wishlist.objects.get_or_create(user=request.user)
    
    if product not in wishlist.products.all():
        wishlist.products.add(product)
        messages.success(request, f"{product.name} was added to your wishlist!")
    else:
        messages.info(request, "This product is already in your wishlist.")

    
    next_url = request.GET.get('next', '')
    if next_url:
        return redirect(next_url)
    
    return redirect(reverse('product_detail', args=[product_id]))


@login_required
def remove_from_wishlist(request, product_id):
    """
    Remove a product to the user's wishlist.
    """
    product = get_object_or_404(Product, id=product_id)
    wishlist = Wishlist.objects.get(user=request.user)
    if product in wishlist.products.all():
        wishlist.products.remove(product)
        messages.success(request, f"{product.name} was removed from your wishlist.")
    return redirect("wishlist")
