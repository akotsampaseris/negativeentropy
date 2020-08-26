from django.contrib import admin
from .models import Post, PostCategory

class PostAdmin(admin.ModelAdmin):
    pass


class PostCategoryAdmin(admin.ModelAdmin):
    pass


admin.site.register(Post, PostAdmin)
admin.site.register(PostCategory, PostCategoryAdmin)
