from django.db import models
from profiles.models import UserProfile
from django.utils.text import slugify
from cloudinary.models import CloudinaryField
from django.contrib.auth.models import User


class Post(models.Model):

    STATUS = ((0, "Draft"), (1, "Published"), (2, "Archived"))

    title = models.CharField(max_length=255)
    slug = models.SlugField(unique=True, blank=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="blog_posts")
    featured_image = CloudinaryField('image', default='blog_placeholder')
    excerpt = models.TextField(blank=True)
    content = models.TextField()
    date_posted = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=10, choices=STATUS, default='draft')

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    class Meta:
        verbose_name_plural = "Posts"
        ordering = ["-date_posted"]

    def __str__(self):
        return self.title

