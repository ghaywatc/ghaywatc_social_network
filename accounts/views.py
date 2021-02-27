from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView
from accounts import form

class Signup(CreateView):
    form_class = form.UserCreateForm
    success_url = reverse_lazy("login")
    template_name = "accounts/signup.html"