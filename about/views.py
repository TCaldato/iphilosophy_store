from django.contrib import messages
from django.shortcuts import render
from .models import About
from .forms import CollaborateForm


def about_me(request):
    """Handles the 'About Me' page requests, displays
    the latest 'About' section and a form for
    collaboration requests.
    """
    if request.method == "POST":
        collaborate_form = CollaborateForm(data=request.POST)
        if collaborate_form.is_valid():
            collaborate_form.save()
            messages.add_message(
                request,
                messages.SUCCESS,
                "Collaboration request received! I will respond you within 2 working days.",
            )

    # Ensure About has the 'objects' manager correctly available
    about = About.objects.all().order_by("-updated_on").first()
    # Initialize a blank form for GET requests
    collaborate_form = CollaborateForm()

    return render(
        request,
        "about/about.html",
        {"about": about, "collaborate_form": collaborate_form},
    )
