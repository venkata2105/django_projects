"""
URL configuration for blogproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from blog import views


urlpatterns: list = [
    path('admin/', admin.site.urls),  # Admin URL
    path('post/', views.get_post_data),  # Endpoint for getting post data
    path('register/', views.user_registration),  # Endpoint for user registration
    path('login/', views.login_user),  # Endpoint for user login
    path('postdata/', views.get_posts),  # Endpoint for getting posts (for logged-in users)
    path('logout/', views.user_logout),  # Endpoint for user logout
]
