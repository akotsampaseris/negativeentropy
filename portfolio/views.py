from django.shortcuts import render

from .models import Website, WebsiteCategory

# Create your views here.
def index(request):
    cats = WebsiteCategory.objects.all()
    websites = Website.objects.all()

    context = {
        "cats": cats,
        "websites": websites,
    }

    return render(request, 'portfolio/index.html', context)
