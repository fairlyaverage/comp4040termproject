from django.shortcuts import render, redirect
from django.views import generic # class-based
from .models import Moment #, Momenteer
from django.http import HttpResponseRedirect
from django.urls import reverse
# from django.contrib.auth.forms import UserCreationForm

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

from django.contrib.auth.forms import UserCreationForm
from .forms import CustomUserCreationForm #, CreateMomentForm
from django.contrib import messages

def register(request):

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

# def new_moment(request):
#     if request.method == 'POST':
#         form = CreateMomentForm(request.POST)
#         if form.is_valid():
#             new_moment = Moment
#             new_moment.moment_text = form.cleaned_data['moment_text']
#             new_moment.moment_created = form.cleaned_data['moment_created']
#             new_moment.moment_by = user
#             form.save()
#             return HttpResponseRedirect(reverse('mymoments'))
#     else:
#         form = CreateMomentForm()

#     context = {
#         'form': form
#     }
#     return render(request, 'new_moment.html', context)

# from mymoments.forms import UserForm # mymoments.forms?

# def signup(request):
#     # after user submitted something (post) or initial form (get)
#     if requesUserCreationFormt.method == 'POST':
#         form = UserForm(request.POST)
#         if form.is_valid():
#             form.save()
#             # troubleshooting
#             return HttpResponseRedirect(reverse('login')) # where should new users go, maybe all-moments or be prompted to sign in?
#             # return redirect('all-moments')
#     else: # first time
#         form = UserForm()

#     return (request, 'signup.html', {'form': form}) # note last argument is a dictionary, could define and use context

# more old and bad
# from django.contrib.auth.decorators import login_required
# # from django.contrib.auth.forms import UserCreationForm
# from .forms import SnippetForm, ContactForm, LoginForm

# def signup(request):

#     if request.user.is_authenticated:
#         return redirect('allmoments', username=request.user.username)

#     if request.method == 'POST':
#         f = UserCreationForm(request.POST)
#         if f.is_valid():
#             f.save()
#             messages.success(request, 'Account created successfully')
#             return redirect('signup')
#     else:
#         f = UserCreationForm()

#     return render(request, 'signup.html', {'form': f})



# OLD, BAD
# def signup(request):
#     new_momenteer = Momenteer

#     if request.method == 'POST':
#         # user tried to submit form
#         form = UserCreationForm(request.POST)

#         if form.is_valid():
#             new_momenteer.username = form.cleaned_data['username']
#             new_momenteer.password = form.cleaned_data['password']
#             new_momenteer.email = form.cleaned_data['email']
#             new_momenteer.first_name = form.cleaned_data['first_name']
#             new_momenteer.last_name = form.cleaned_data['last_name']
#             new_momenteer.save()
#             return HttpResponseRedirect(reverse('all-moments'))
#     else:
#         # get request; initial form
#         form = UserCreationForm()

#     context = {
#         'form': form,
#         'new_momenteer': new_momenteer,
#     }

#     return render(request, 'signup.html', context)
