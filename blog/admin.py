from django.contrib import admin
from .models import Post
# Register your models here.


# admin.site.register(Post)
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    # define which columns have to be show in the table
    list_display = ('title', 'slug', 'publish', 'author')
    list_filter = ('status', 'created', 'author', 'publish')
    search_fields = ('title', 'body')
    prepopulated_fields = {'slug': ('title',)}
    raw_id_fields = ('author',)
    date_hierarchy = 'publish'
    ordering = ('status', 'publish')