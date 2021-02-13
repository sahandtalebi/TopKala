from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from .forms import RegisterForm, LoginForm, RegisterForm
from django import views


def login_page(request):
    if request.user.is_authenticated:
        return redirect('/')

    login_form = LoginForm(request.POST or None)

    if login_form.is_valid():
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/admin')
    context = {
        'login_form': login_form
    }
    return render(request, 'login.html', context)


def register_page(request):
    if request.user.is_authenticated:
        return redirect('/')
    register_form = RegisterForm(request.POST or None)

    if register_form.is_valid():
        username = request.POST['username']
        password = request.POST['password']
        email = request.POST['email']
        User.objects.create(username=username, password=password, email=email)
    context = {
        'form': register_form
    }
    return render(request, 'register.html', context)