from django.contrib import admin

# Register your models here.
from .models import Post, PostCategory


class PostAdmin(admin.ModelAdmin):
    list_display            = ('title', 'slug')
    prepopulated_fields     = {'slug': ('title',)}

admin.site.register(Post, PostAdmin)
admin.site.register(PostCategory)