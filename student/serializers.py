from rest_framework import serializers
from .models import *
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'password']
    '''password hashing overriding method'''
    def create(self, validated_data):
        user = User.objects.create_user(username=validated_data['username'])
        user.set_password(validated_data['password'])
        user.save()
        return user


class Student_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Student_data
        fields = "__all__"
