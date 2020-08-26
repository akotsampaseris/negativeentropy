from django.contrib import admin
from .models import Website, WebsiteCategory

class WebsiteAdmin(admin.ModelAdmin):
    pass


class WebsiteCategoryAdmin(admin.ModelAdmin):
    pass


admin.site.register(Website, WebsiteAdmin)
admin.site.register(WebsiteCategory, WebsiteCategoryAdmin)
