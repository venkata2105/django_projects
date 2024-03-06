from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [path("student/",  StudentApi.as_view()),
               path("register/",  Registration.as_view())]
