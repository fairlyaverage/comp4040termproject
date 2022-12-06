from django.shortcuts import render, redirect
from django.views import generic
from .models import Moment
from django.http import HttpResponseRedirect
from django.urls import reverse, reverse_lazy
from django.contrib.auth.decorators import login_required
import datetime
from .forms import CustomUserCreationForm, CreateMomentForm
from django.contrib import messages

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

def register(request):
    if request.user: # don't let users try to create another account
        return HttpResponseRedirect(reverse('login'))

    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)

        if form.is_valid():
            # save one time dummy
            # new_user = form.save(commit=False)
            # new_user.set_password(form.cleaned_data.get('password'))
            # new_user.save()
            form.save()
            return HttpResponseRedirect(reverse('login'))
        messages.success(request, 'Account created')
    else:
        form = CustomUserCreationForm()
    context = {
        'form': form
    }
    return render(request, 'signup.html', context)

@login_required
def new_moment(request):
    if request.method == 'POST':
        form = CreateMomentForm(request.POST)
        if form.is_valid():
            new_moment = form.save(commit=False)
            new_moment.moment_text = form.cleaned_data['moment_text']
            new_moment.moment_created = datetime.datetime.now()
            new_moment.moment_edited = None
            new_moment.moment_by = request.user
            form.save()
            return HttpResponseRedirect(reverse('my_moments'))
    else:
        form = CreateMomentForm()
    context = {
        'form': form
    }
    return render(request, 'new_moment.html', context)
