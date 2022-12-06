from django.shortcuts import render, redirect, get_object_or_404
from django.views import generic
from .models import Moment
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse, reverse_lazy
from django.contrib.auth.decorators import login_required
import datetime
from .forms import CustomUserCreationForm, CreateMomentForm, UpdateMomentForm
from django.contrib import messages


def index(request):

    context = {} # empty placeholder

    return render(request, 'index.html', context=context)

class AllMoments(generic.ListView):
    model = Moment

class MyMoments(generic.ListView):
    model = Moment
    template_name = 'mymoments/mymoments_list.html'

# class Moment(generic.DetailView):
#     model = Moment

def register(request):
    if request.user.is_authenticated: # don't let users try to create another account
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

def moment(request, pk):
    context = {}
    context["moment"] = Moment.objects.get(id=pk)
    return render(request, "moment.html", context)

@login_required
def update_moment(request, pk):
    template = "update_moment.html"
    moment = get_object_or_404(Moment, id=pk)
    if request.user != moment.moment_by:
        messages.warning(request, "You do not have permission to edit this Moment")
        return HttpResponseRedirect(reverse('all_moments'))

    form = UpdateMomentForm(request.POST or None, instance = moment)

    if form.is_valid():
        updated_moment = form.save(commit=False)
        updated_moment.moment_edited = datetime.datetime.now()
        form.save()
        return HttpResponseRedirect(reverse('my_moments'))

    context = {}
    context["form"] = form

    return render(request, "update_moment.html", context)
