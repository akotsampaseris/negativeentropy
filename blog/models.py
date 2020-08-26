from django.db import models
from django.utils.text import slugify

# Create your models here.
class PostCategory(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True, blank=True)
    description = models.TextField(blank=True)

    class Meta:
        verbose_name = 'Post Category'
        verbose_name_plural = 'Post Categories'

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(PostCategory, self).save(*args, **kwargs)

    def __str__(self):
        return self.name


class Post(models.Model):
    title = models.CharField(max_length=100)
    category = models.ForeignKey(PostCategory, on_delete=models.CASCADE, blank=True)
    slug = models.SlugField(unique=True, blank=True)
    text = models.TextField(blank=True)
    image = models.ImageField(blank=True, upload_to="blog/images/")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    published = models.BooleanField(default=False)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Post, self).save(*args, **kwargs)


    def __str__(self):
        return self.title
