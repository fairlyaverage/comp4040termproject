from django.shortcuts import render
from django.views import generic # class-based
from .models import Moment

def index(request):

    context = {} # empty placeholder

    return render(request, 'index.html', context=context)

class AllMoments(generic.ListView):
    model = Moment

class MyMoments(generic.ListView):
    model = Moment
    template_name = 'mymoments/mymoments_list.html'

class Moment(generic.DetailView):
    model = Moment
