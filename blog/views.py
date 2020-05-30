
from django.shortcuts import render
from django.views.generic import ListView,TemplateView
from .models import Blog
# Create your views here.
class BlogList(ListView):
    template_name = 'blog.html'
    model = Blog
    paginate_by = 8
     

class Blog1(TemplateView):
    template_name = '1.html'
