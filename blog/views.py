from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.core.serializers import serialize
from . forms import Registration, Login
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from.models import *
from django.contrib.auth.decorators import login_required



def get_post_data(request):
    post = Post.objects.all()
    data = serialize('json', post)
    return HttpResponse(data)


def user_registration(request):
    if request.method == 'POST':
        form = Registration(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            mail = form.cleaned_data['email']
            password = form.cleaned_data['password']
            user = User.objects.create_user(username=username, email=mail, password=password)
            print('user created succesfully')
            return render(request, 'registration.html', {'form': form})


    else:
        form = Registration()
        return render(request, 'registration.html', {'form': form})


def login_user(request):
    form = Login(request.POST)
    if request.method == "POST":
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                Login(request, user)
                print('hello {user} welcome you logged in succesfully')
                return None
            else:
                form = Registration()
                return render(request, 'registration.html', {'form': form})
    else:
        form = Login()
        return render(request, 'login.html', {'form': form})


def user_logout(request):
    logout(request)

@login_required()
def get_posts(request):
    post_data = Post.objects.all()
    json_data = serialize('json', post_data)
    return HttpResponse(json_data)










