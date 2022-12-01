from django.shortcuts import render
from django.views import generic # class-based
from .models import Moment, Momenteer
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.forms import UserCreationForm

def index(request):

    context = {} # empty placeholder

    return render(request, 'index.html', context=context)

def signup(request):
    new_momenteer = Momenteer

    if request.method == 'POST':
        # user tried to submit form
        form = UserCreationForm(request.POST)

        if form.is_valid():
            new_momenteer.username = form.cleaned_data['username']
            new_momenteer.password = form.cleaned_data['password']
            new_momenteer.email = form.cleaned_data['email']
            new_momenteer.first_name = form.cleaned_data['first_name']
            new_momenteer.last_name = form.cleaned_data['last_name']
            new_momenteer.save()
            return HttpResponseRedirect(reverse('all-moments'))
    else:
        # get request; initial form
        form = UserCreationForm()

    context = {
        'form': form,
        'new_momenteer': new_momenteer,
    }

    return render(request, 'signup.html', context)

class AllMoments(generic.ListView):
    model = Moment

class MyMoments(generic.ListView):
    model = Moment
    template_name = 'mymoments/mymoments_list.html'

class Moment(generic.DetailView):
    model = Moment
