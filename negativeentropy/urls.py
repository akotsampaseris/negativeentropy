from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # Django URLs
    path('admin/', admin.site.urls),
    # Custom URLs
    path('', include('pages.urls')),
    path('blog/', include('blog.urls')),
    path('cv/', include('cv.urls')),
    path('portfolio/', include('portfolio.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
