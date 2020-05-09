from django.shortcuts import render
from blog.models import Blog
from contact.forms import Contact
import os
# Create your views here.

from django.views.generic import TemplateView


class Home(TemplateView):
    template_name = "home.html"
    blog1 = Blog.objects.get(blog_id=1)
    blog_title1 = blog1.blog_title
    blog_desc1 = blog1.blog_desc
    blog2 = Blog.objects.get(blog_id=2)
    blog_title2 = blog2.blog_title
    blog_desc2 = blog2.blog_desc
    extra_context = {'title1': blog_title1 , 'desc1': blog_desc1,'title2': blog_title2 , 'desc2': blog_desc2 , 'form':Contact}

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     result = Blog.objects.raw('select blog_id , blog_desc from blog_blog where blog_id=1')
    #     context = result
    #
    # def get_queryset(self):
    #     queryset  = Blog.objects.get(blog_id=1)
    #     #Blog.objects.raw('select blog_desc from blog_blog where blog_id=1')
    #     return queryset
