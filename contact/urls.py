from django.conf.urls import url
from django.urls import path , re_path
from .views import Contactus


app_name = 'contact'

urlpatterns = [
    path('', Contactus.as_view()),
]
