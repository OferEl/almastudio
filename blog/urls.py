from django.conf.urls import url
from django.urls import path , re_path
from .views import BlogList,Blog1


app_name = 'blog'

urlpatterns = [
    path('', BlogList.as_view()),
    path('1', Blog1.as_view()),
]
