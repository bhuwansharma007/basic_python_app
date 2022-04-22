from django.shortcuts import render
from rest_framework.response import Response
from .models import *
from .serializer import *
from rest_framework.generics import GenericAPIView


from django.http import HttpResponse

from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions  import IsAuthenticated


# Create your views here.

class Task_Check(GenericAPIView):
    authentication_classes = [IsAuthenticated]
    permission_classes = [JWTAuthentication]

    Serializer_class = TaskSerializer

    def get(self,request):
        objects = Task.objects.all()
        Serializer_class = TaskSerializer(objects,many=True)
        return Response(serializers.data)

    def post(self,request):
        data = request.data
        obj = Task.objects.create(title=data['title'],description=data['description'],task=data['task'],status=data['status'])
        return HttpResponse("Object is Created")






























# for api testing purposes 
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView

class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        # Add custom claims
        token['name'] = user.name
        # ...

        return token

class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer



