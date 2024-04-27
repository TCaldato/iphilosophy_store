# pylint: disable=invalid-str-returned
from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
    """
    This model stores information about different product categories.
    """

    class Meta:
        """
        Metadata options for the Category model.
        """

        verbose_name_plural = "Categories"

    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        """Return a string representation of the category."""
        return self.name

    def get_friendly_name(self):
        """Get the friendly name of the category."""
        return self.friendly_name


class Product(models.Model):
    """
    This model stores information about different products.
    """

    category = models.ForeignKey(
        "Category", null=True, blank=True, on_delete=models.SET_NULL
    )
    sku = models.CharField(max_length=254, null=True, blank=True)
    name = models.CharField(max_length=254)
    author = models.CharField(max_length=254, default="author")
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    rating = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        """Return a string representation of the product."""
        return self.name


class Review(models.Model):
    """This model stores information about reviews of products."""

    product = models.ForeignKey(
        Product, related_name="reviews", on_delete=models.CASCADE
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    review_text = models.TextField()
    rating = models.IntegerField(default=1, choices=[(i, str(i)) for i in range(1, 6)])
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        """Metadata options for the Review model."""

        ordering = ["-created_on"]

    def __str__(self):
        return f"Review {self.review_text} by {self.user.username}"


class Wishlist(models.Model):
    """
    Represents a wishlist created by a user.
    """

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="wishlists")
    products = models.ManyToManyField(Product, related_name="wishlisted_by")

    def __str__(self):
        return f"Wishlist of {self.user.username}"
