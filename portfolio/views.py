from django.shortcuts import render

from .models import Website, WebsiteCategory

# Create your views here.
def index(request):
    work_cat = WebsiteCategory.objects.get(name='Work')
    side_cat = WebsiteCategory.objects.get(name='Side Projects')
    work_websites = Website.objects.filter(category=work_cat)
    side_websites = Website.objects.filter(category=side_cat)

    context = {
        "work_websites": work_websites,
        "side_websites": side_websites,
    }

    return render(request, 'portfolio/index.html', context)
