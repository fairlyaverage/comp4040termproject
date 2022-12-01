from django import forms

from mymoments.models import Momenteer

class Signup(forms.ModelForm):
    class Meta:
        model = User
        # fields = ('first_name', 'last_name', 'email')

class Momenteer(forms.ModelForm):
    class Meta:
        model = Momenteer
        # fields = ('url', 'location', 'company')

# class Signup(forms.Form):

#     model = Momenteer

#     username = CharField(max_length=150, help_text='Enter a username')
#     email = EmailField(max_length=254, help_text='Enter your email address')
#     password = CharField(max_length=128, help_text='Enter a password')
#     password_confirm = CharField(max_length=128, help_text='Confirm password')

#     first_name = CharField(max_length=150, help_text='Your first name')
#     last_name = CharField(max_length=150, help_text='Your last name')
