from django.shortcuts import render
from .models import Report
from rest_framework.views import APIView
from .serializers import ReportSerializer
from rest_framework.response import Response
from rest_framework.permissions import IsAdminUser

# Create your views here.



class ReportView(APIView):
    permission_classes = (IsAdminUser,)
    def get(self,request,*args,**kwargs):
        pk = kwargs.get('pk')
        if pk:
            queryset = Report.objects.get(id = pk)
        else:
            queryset = Report.objects.all()
        serializer = ReportSerializer(queryset,many=True)
        return Response(serializer.data)