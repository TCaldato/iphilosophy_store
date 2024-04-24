from django.db import models


class About(models.Model):
    """
    Represents an 'About' section for Iphilosophy
    e-commerce.
    """

    title = models.CharField(max_length=200)
    updated_on = models.DateTimeField(auto_now=True)
    content = models.TextField()

    def __str__(self):
        # Ensures the title is returned as a string.
        return str(self.title)


class CollaborateRequest(models.Model):
    """
    Model to handle collaboration requests
    submitted through the website.
    """

    name = models.CharField(max_length=200)
    email = models.EmailField()
    message = models.TextField()
    read = models.BooleanField(default=False)

    def __str__(self):
        # Provides a clear description in the admin view.
        return f"Collaboration request from {self.name}"
