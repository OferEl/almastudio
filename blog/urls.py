from django.conf.urls import url
from django.urls import path , re_path
from .views import BlogList


app_name = 'blog'

urlpatterns = [
    path('', BlogList.as_view()),
]
