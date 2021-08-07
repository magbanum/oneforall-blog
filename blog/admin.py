from blog.models import Post, Tag
from django.contrib import admin

# Register your models here.
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'status', 'created_on')
    list_filter = ('status',)
    search_fields = ['title', 'content']
    prepopulated_fields = {'slug': ('title',)}

# class TagAdmin(admin.ModelAdmin):
#     list_display = ('title', 'slug', 'created_on')
#     search_fields = ['title']
#     prepopulated_fields = {'slug': ('title',)}

admin.site.register(Post, PostAdmin)
admin.site.register(Tag)
