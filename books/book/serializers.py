<<<<<<< HEAD
from rest_framework import serializers
from .models import Book_Model


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book_Model
        fields = '__all__'
=======
from rest_framework import serializers
from .models import Book_Model


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book_Model
        fields = '__all__'
>>>>>>> 1d221d9c65af698a7761a514f421d3a52566b2c1
