from django.contrib import admin
from .models import Post


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    """
    A class for rendering the Post model in the admin panel.
    """

    fields = ('title', 'slug', 'author', 'featured_image',
              'status', 'content')

    list_filter = ('status', 'author')

    list_display = ('title', 'author', 'date_posted', 'status')

    search_fields = ('title', 'content')

    ordering = ('-date_posted',)
