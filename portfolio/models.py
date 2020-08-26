from django.db import models

# Create your models here.
class WebsiteCategory(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)

    class Meta:
        verbose_name = 'Website Category'
        verbose_name_plural = 'Website Categories'

    def __str__(self):
        return self.name


class Website(models.Model):
    url = models.URLField(max_length=100)
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=100, blank=True)
    category = models.ForeignKey(WebsiteCategory, on_delete=models.CASCADE, blank=True)
    image = models.ImageField(max_length=100, blank=True, upload_to="portfolio/images/")
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)
    published = models.BooleanField(default=False)

    def __str__(self):
        return self.title
