from django.shortcuts import render ,redirect
from django.views.generic import ListView , FormView
from .models import Forum
from .forms import Newtopic



# Create your views here.
class Forumlist(ListView):
    template_name = 'forum.html'
    model = Forum
    paginate_by = 8


def topic(request):
    if request.method == "POST":
        form = Newtopic(request.POST)
        form.full_clean()
        v = form.is_valid()
        if v :
            form.save()
            return redirect('/forum/list')
    else:
        form=Newtopic()


