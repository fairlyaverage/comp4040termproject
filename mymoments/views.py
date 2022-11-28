from django.shortcuts import render
from .models import Moment

def index(request):

    context = {} # empty placeholder

    return render(request, 'index.html', context=context)
