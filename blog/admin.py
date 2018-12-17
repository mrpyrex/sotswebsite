from django.contrib import admin

# Register your models here.
from .models import Post, Comment


class PostAdmin(admin.ModelAdmin):
    list_display            = ('title', 'slug')
    prepopulated_fields     = {'slug': ('title',)}

admin.site.register(Post, PostAdmin)

class CommentAdmin(admin.ModelAdmin):
    list_display    = ('comment_author', 'email', 'post', 'date', 'active')
    list_filter     = ('active', 'date')
    search_fields   = ('comment_author', 'email', 'body')

admin.site.register(Comment, CommentAdmin)