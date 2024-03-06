<<<<<<< HEAD
from django.contrib import admin
from django.urls import path
from .views import book_list, book_post, book_get, book_update

urlpatterns = [
    path("list/", book_list),
    path("add/", book_post),
    path("read/<int:pk>/", book_get),
    path("update/<int:pk>/", book_update),
]
=======
from django.contrib import admin
from django.urls import path
from .views import book_list, book_post, book_get, book_update

urlpatterns = [
    path("list/", book_list),
    path("add/", book_post),
    path("read/<int:pk>/", book_get),
    path("update/<int:pk>/", book_update),
]
>>>>>>> 1d221d9c65af698a7761a514f421d3a52566b2c1
