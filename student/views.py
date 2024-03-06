from django.shortcuts import render
from rest_framework.decorators import APIView, api_view
from rest_framework.response import Response
from .serializers import Student_Serializer, UserSerializer
from .models import Student_data
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated


class Registration(APIView):
    def post(self, request):
        serialize = UserSerializer(data=request.data)
        if serialize.is_valid():
            serialize.save()
            user = User.objects.get(username=serialize.data['username'])
            token_obj, _ = Token.objects.get_or_create(user=user)
            return Response({'status': 200, 'payload': serialize.data, 'token': str(token_obj)})
        else:
            return Response({'status': 400, 'errors': serialize.errors})


class StudentApi(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        std_obj = Student_data.objects.all()
        std_serialize = Student_Serializer(std_obj, many=True)
        return Response({'status': 200, 'payload': std_serialize.data})

    def post(self, request):
        post_data = request.data
        post_serialize = Student_Serializer(data=post_data)
        if not post_serialize.is_valid():
            print(post_serialize.errors)
            return Response({'status': 403, 'errors': post_serialize.errors, 'message': 'Something went wrong'})

        else:
            post_serialize.save()
            return Response({'status': 200, 'payload': post_serialize.data})

    def patch(self, request):
        try:
            patch_obj = Student_data.objects.get(id=request.data['id'])
            serialize = Student_Serializer(patch_obj, data=request.data, partial=True)
            if not serialize.is_valid():
                print(serialize.errors)
                return Response({'status': 403, 'errors': serialize.errors, 'message': 'Something went wrong'})
            else:
                serialize.save()
                return Response({'status': 200, 'payload': serialize.data})
        except Student_data.DoesNotExist:
            return Response({'status': 404, 'message': 'Student not found'})
        except Exception as e:
            print(e)
            return Response({'status': 500, 'message': 'Internal Server Error'})
