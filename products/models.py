from django.db import models


class Category(models.Model):
    """
    Represents a category for products in the database.
    """

    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)

    class Meta:
        """
        Overrides the default plural form in Django admin.
        """

        verbose_name_plural = "Categories"

    def __str__(self):
        return str(self.name)

    def get_friendly_name(self):
        """
        Provides the friendly name of the category for use in user interfaces.
        """
        return self.friendly_name


class Product(models.Model):
    """
    Represents a product stored in the database.
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
        return str(self.name)
