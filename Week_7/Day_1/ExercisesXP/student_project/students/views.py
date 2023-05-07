from django.shortcuts import render
from .models import Student
from rest_framework.views import APIView
from .serializers import StudentSerializer
from rest_framework.response import Response
from rest_framework.permissions import IsAdminUser
from rest_framework.status import (HTTP_200_OK, HTTP_201_CREATED, HTTP_400_BAD_REQUEST , HTTP_202_ACCEPTED)

# Create your views here.



class StudentView(APIView):
    permission_classes = (IsAdminUser,)
    def get(self,request,*args,**kwargs):
        pk = kwargs.get('pk')
        if pk:
            try:
                queryset = Student.objects.get(id = pk)
                serializer = StudentSerializer(queryset)
            except Student.DoesNotExist:
                return Response({'details': 'post not found'}, status=HTTP_400_BAD_REQUEST)
        else:
            queryset = Student.objects.all()
            serializer = StudentSerializer(queryset,many=True)
        
        return Response(serializer.data)
    def post(self,request,*args,**kwargs):
        serializer = StudentSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data , status = HTTP_200_OK)
        return Response(serializer.errors , status = HTTP_400_BAD_REQUEST)
    def delete(self ,request, pk , *args,**kwargs):
        try:
            student = Student.objects.get(id = pk)
            student.delete()
            return Restponse({'details': 'post deleted'}, status =HTTP_202_ACCEPTED)
        except:
            return Response({'details': 'post not found'}, status=HTTP_400_BAD_REQUEST)
    def put(self ,request, *args,**kwargs):
        pk = kwargs.get('pk')

        if pk:
            try:
                post = Student.objects.get(id=pk)
                serializer = StudentSerializer(post , data=request.data)
                if serializer.is_valid():
                    serializer.save()
                    return Response(serializer.data , status=HTTP_202_ACCEPTED)
            except Student.DoesNotExist:
                return Response({"detail":"Post Not Found"} , status=HTTP_400_BAD_REQUEST)

        else:
            return Response({"detail":"PK Not Found"} , status=HTTP_400_BAD_REQUEST)