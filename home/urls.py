from django.conf.urls import url
from django.urls import path , re_path
from .views import Home


app_name = 'home'

urlpatterns = [
    path('', Home.as_view()),
]
