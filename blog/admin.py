from blog.forms import PostForm
from django.db import models
from blog.models import Post, Tag
from django.contrib import admin
from markdownx.admin import MarkdownxModelAdmin
from markdownx.widgets import AdminMarkdownxWidget
# Register your models here.
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'status', 'created_on')
    list_filter = ('status',)
    search_fields = ['title', 'content']
    prepopulated_fields = {'slug': ('title',)}
    formfield_overrides = {
        models.TextField: {'widget': AdminMarkdownxWidget},
    }

class TagAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_on')
    search_fields = ['title']
    

admin.site.register(Post, PostAdmin)
admin.site.register(Tag, TagAdmin)
