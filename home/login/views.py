from django.shortcuts import render
from rest_framework.response import Response
from .models import *
from .serializer import *
from rest_framework.generics import GenericAPIView


from django.http import HttpResponse

from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated


# Create your views here.

class Task_Check(GenericAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    Serializer_class = TaskSerializer
    # to view the Task
    def get(self,request):
        objects = Task.objects.all()
        serializer = TaskSerializer(objects,many=True)
        return Response(serializer.data)
    # to create Task
    def post(self,request):
        data = request.data
        obj = Task.objects.create(title=data['title'],description=data['description'],task=data['task'],status=data['status'])
        return HttpResponse("Object is Created")

    # to remove the task
    def delete(self,request):
        try:
            title = request.GET.get('title')
            task_obj = Task.objects.filter(id = title)
            task_obj.delete()
            return Response({'status':200,'message':'deleted'})

        except Exception as e :
            return Response({'status':403,'message':'title is not present in DB'})

    # to update the task
    def patch(self,request):
        try:
            task_obj = Task.objects.get(title = request.data['title'])

            serializer = TaskSerializer(task_obj,data=request.data,partial=True)
            if not serializer.is_valid():
                return Response({'status':403,'errors':serializer.data, 'message':'Somethings went wrong'})
            serializer.save()
            return Response({'status':200,'payload':serializer.data,'message':'your data is saved'})

        except Exception as e:
            return Response({'status':403,'message':'invalid title '})

































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



