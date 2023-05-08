from rest_framework import serializers
from .models import Employee , Task , Project , Department


class EmployeeSerializer(serializers.ModelSerializer):
    employee = serializers.HyperlinkedIdentityField(view_name='employee')
    class Meta:
        model = Employee
        fields = '__all__'
class DepartmentSerializer(serializers.ModelSerializer):
    department = serializers.HyperlinkedIdentityField(view_name='department')
    class Meta:
        model = Department
        fields = '__all__'
class TaskSerializer(serializers.ModelSerializer):
    task = serializers.HyperlinkedIdentityField(view_name='task')
    class Meta:
        model = Task
        fields = '__all__'
class ProjectSerializer(serializers.ModelSerializer):
    project = serializers.HyperlinkedIdentityField(view_name='project')
    class Meta:
        model = Project
        fields = '__all__'