
from django.views.generic import viewsets
from management.models import Department , Employee
from management.serializers import DepartmentSerializer , EmployeeSerializer
from rest_framework import DefaultRouter
from rest_framework.response import Response
class DepartmentViewSet(viewsets.ModelViewSet):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer
class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    def list(self,request):
        return Response(serializer_class.data)