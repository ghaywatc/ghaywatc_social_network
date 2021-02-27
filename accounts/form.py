from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User
class UserCreateForm(UserCreationForm):
   username= forms.CharField(max_length=250)
   email= forms.EmailField()
   mobile= forms.IntegerField()
   country= forms.CharField(max_length=250)

   class Meta():
       model= User
       fields= [
           'username',
           'email',
           'mobile',
           'country',
           'password1',
           'password2'
       ]


