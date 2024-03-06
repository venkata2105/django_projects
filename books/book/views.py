<<<<<<< HEAD
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Book_Model
from .serializers import BookSerializer
from django.shortcuts import get_object_or_404


# READ
@api_view(['GET'])
def book_list(request):
    book_obj = Book_Model.objects.all()
    print(book_obj)
    serialize_obj = BookSerializer(book_obj, many=True)
    return Response(serialize_obj.data)


# Post
@api_view(['POST'])
def book_post(request):
    # Check if request data is provided and is a list
    if isinstance(request.data, list):
        serialize = BookSerializer(data=request.data, many=True)
        print(serialize)
        if serialize.is_valid():
            serialize.save()
            return Response(serialize.data)
        else:
            return Response(serialize.errors)
    else:
        # Return error response if request data is not a list
        return Response({"error": "Invalid data format. Expected a list."}, status=400)


# read_data


@api_view(['GET'])
def book_get(request, pk):
    book_data = get_object_or_404(Book_Model.objects.filter(pk=pk))
    print(book_data)
    print(type(book_data))
    serialize = BookSerializer(book_data)
    return Response(serialize.data)


# update_data
@api_view(['POST'])
def book_update(request, pk):
    book = get_object_or_404(Book_Model.objects.filter(pk=pk))
    book_serialize = BookSerializer(book, data=request.data)
    print(book_serialize)
    if book_serialize.is_valid():
        book_serialize.save()
        return Response(book_serialize.data)
    else:
        return Response(book_serialize.errors)


# delete record


def delete_book(request, pk):
    book = get_object_or_404(Book_Model.objects.filter(pk=pk))
    book.delete()
    return Response({'message': 'record deleted sucessfully'})
=======
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Book_Model
from .serializers import BookSerializer
from django.shortcuts import get_object_or_404


# READ
@api_view(['GET'])
def book_list(request):
    book_obj = Book_Model.objects.all()
    print(book_obj)
    serialize_obj = BookSerializer(book_obj, many=True)
    return Response(serialize_obj.data)


# Post
@api_view(['POST'])
def book_post(request):
    # Check if request data is provided and is a list
    if isinstance(request.data, list):
        serialize = BookSerializer(data=request.data, many=True)
        print(serialize)
        if serialize.is_valid():
            serialize.save()
            return Response(serialize.data)
        else:
            return Response(serialize.errors)
    else:
        # Return error response if request data is not a list
        return Response({"error": "Invalid data format. Expected a list."}, status=400)


# read_data


@api_view(['GET'])
def book_get(request, pk):
    book_data = get_object_or_404(Book_Model.objects.filter(pk=pk))
    print(book_data)
    print(type(book_data))
    serialize = BookSerializer(book_data)
    return Response(serialize.data)


# update_data
@api_view(['POST'])
def book_update(request, pk):
    book = get_object_or_404(Book_Model.objects.filter(pk=pk))
    book_serialize = BookSerializer(book, data=request.data)
    print(book_serialize)
    if book_serialize.is_valid():
        book_serialize.save()
        return Response(book_serialize.data)
    else:
        return Response(book_serialize.errors)


# delete record


def delete_book(request, pk):
    book = get_object_or_404(Book_Model.objects.filter(pk=pk))
    book.delete()
    return Response({'message': 'record deleted sucessfully'})
>>>>>>> 1d221d9c65af698a7761a514f421d3a52566b2c1
