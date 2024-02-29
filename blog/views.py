from typing import Any
from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
from django.core.serializers import serialize
from .forms import Registration, Login
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from .models import Post
from django.contrib.auth.decorators import login_required


def get_post_data(request: HttpRequest) -> HttpResponse:
    """Get serialized post data.

    Args:
        request (HttpRequest): Django HTTP request object.

    Returns:
        HttpResponse: Serialized post data as JSON response.
    """
    posts = Post.objects.all()
    data = serialize('json', posts)
    return HttpResponse(data)


def user_registration(request: HttpRequest) -> Any:
    """ Handles user registration.

    Args:
        request (HttpRequest): Django HTTP request object.

    Returns:
        Any: Rendered registration form or None.
    """
    if request.method == 'POST':
        form = Registration(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            user = User.objects.create_user(username=username, email=email, password=password)
            print('User created successfully')
            return render(request, 'registration.html', {'form': form})
    else:
        form = Registration()
    return render(request, 'registration.html', {'form': form})


def login_user(request: HttpRequest) -> Any:
    """handles user login.

    Args:
        request (HttpRequest): Django HTTP request object.

    Returns:
        Any: Renders login form.
    """
    form = Login(request.POST)
    if request.method == "POST":
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                print(f'Hello {user}, welcome. You have logged in successfully.')
                return None
            else:
                form = Registration()
    else:
        form = Login()
    return render(request, 'login.html', {'form': form})


def user_logout(request: HttpRequest) -> None:
    """Handles user logout.

    Args:
        request (HttpRequest): Django HTTP request object.
    """
    logout(request)


@login_required()
def get_posts(request: HttpRequest) -> HttpResponse:
    """Get serialized post data for logged-in users.

    Args:
        request (HttpRequest): Django HTTP request object.

    Returns:
        HttpResponse: Serialized post data as JSON response.
    """
    posts = Post.objects.all()
    data = serialize('json', posts)
    return HttpResponse(data)
