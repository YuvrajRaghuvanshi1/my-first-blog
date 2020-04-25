from django.contrib.auth import login, logout
from django.urls import reverse_lazy
from django.views.generic import CreateView
from . import forms
from django.shortcuts import render,get_object_or_404, redirect

# Create your views here.
class SignUp(CreateView):
    form_class = forms.UserCreateForm
    success_url = reverse_lazy("accounts:login")
    template_name = "accounts/signup.html"
def profile(request):
    return render(request,'accounts/profile.html')