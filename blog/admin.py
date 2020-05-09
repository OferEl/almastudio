from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Blog

class BlogAdmin(admin.ModelAdmin):
    list_display = ['blog_id', 'blog_type','blog_title','blog_desc'  , 'blog_date' , 'blog_order','blog_text']

admin.site.register(Blog, BlogAdmin)