from django.conf.urls import url
from django.urls import path , re_path
from .views import Forumlist , Newtopic ,topic
from . import views

app_name = 'forum'

urlpatterns = [
    path('list', Forumlist.as_view()),
    path('newtopic', views.topic, name='topic'),

]
