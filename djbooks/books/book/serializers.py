from rest_framework import serializers
from .models import Book_Model


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book_Model
        fields = '__all__'
