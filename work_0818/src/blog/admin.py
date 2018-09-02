from django.contrib import admin
from .models import PostType, Post, Image, File
from django.contrib.contenttypes import fields

# Register your models here.

class PostTypeAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    
class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'type','headline','contents','pub_data','author')
    
class ImageAdmin(admin.ModelAdmin):
    list_display = ('id', 'post','image')
    
class FileAdmin(admin.ModelAdmin):
    list_display = ('id', 'post','file')

admin.site.register(PostType, PostTypeAdmin)
admin.site.register(Post, PostAdmin)
admin.site.register(Image, ImageAdmin)
admin.site.register(File, FileAdmin)