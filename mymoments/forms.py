import datetime
from django import forms
from .models import Moment
# from .models import Momenteer # mymoments.models?
from django.contrib.auth.models import User # get the base User working before a custom one
from django.contrib.auth.forms import UserCreationForm

# OBSOLETE
# class UserForm(UserCreationForm):
#     # UserCreationForm provides parameters:
#     # username...
#     # password1...
#     # password2...

#     # troubleshooting
#     # email = forms.EmailField(max_length=254, help_text='Enter a valid email address', required=False)

#     class Meta:
#         model = User # to-do: Momenteer
#         # troubleshooting
#         # fields = ('username', 'email', 'password1', 'password2') # ordering form fields
#         fields = ('username', 'password1', 'password2')


# maybe use Forms here?

class CreateMomentForm(forms.Form):
    moment = Moment
    moment_text = forms.CharField(help_text="What's going on at this moment?")
    # moment_created = datetime.datetime.now()
    moment_created = forms.DateTimeField(initial=datetime.datetime.now(), disabled=True)
    moment_by = forms.ForeignKeyField

    def clean_moment_text(self): # does this need to be overridden?
        data = self.cleaned_data['moment_text']
        return data

    def clean_moment_created(self):
        data = self.cleaned_data['moment_created']
        return data

    # def save(self, commit=True):
    #     user = current_user







from django.core.exceptions import ValidationError
class CustomUserCreationForm(UserCreationForm):
    username = forms.CharField()
    email = forms.EmailField()
    password1 = forms.CharField()
    password2 = forms.CharField()

    class Meta:
        model = User
        fields = ('username', 'password1', 'password2')

    def clean_username(self):
        username = self.cleaned_data['username'].lower()
        new = User.objects.filter(username = username)
        if new.count():
            raise ValidationError("User already exists")
        return username
    def clean_email(self):
        email = self.cleaned_data['email'].lower()
        new = User.objects.filter(email=email)
        if new.count():
            raise ValidationError("Email already exists")
        return email
    def clean_password2(self):
        password1 = self.cleaned_data['password1']
        password2 = self.cleaned_data['password2']
        if password1 and password2 and password1 != password2:
            raise ValidationError("Passwords don't match")
        return password2

    def save(self, commit=True):
        user = User.objects.create_user(
            self.cleaned_data['username'],
            self.cleaned_data['email'],
            self.cleaned_data['password1']
        )
        return user

# class Signup(forms.ModelForm):
#     class Meta:
#         model = User
#         # fields = ('first_name', 'last_name', 'email')

# class Momenteer(forms.ModelForm):
#     class Meta:
#         model = Momenteer
#         # fields = ('url', 'location', 'company')

# class Signup(forms.Form):

#     model = Momenteer

#     username = CharField(max_length=150, help_text='Enter a username')
#     email = EmailField(max_length=254, help_text='Enter your email address')
#     password = CharField(max_length=128, help_text='Enter a password')
#     password_confirm = CharField(max_length=128, help_text='Confirm password')

#     first_name = CharField(max_length=150, help_text='Your first name')
#     last_name = CharField(max_length=150, help_text='Your last name')
