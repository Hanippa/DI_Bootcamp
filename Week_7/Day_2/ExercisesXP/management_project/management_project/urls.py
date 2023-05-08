"""
URL configuration for management_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path , include
from management.views import (EmployeeListAPIView ,
                            EmployeeCreateAPIView,
                            EmployeeRetrieveAPIView,
                            DepartmentListAPIView,
                            DepartmentCreateAPIView,
                            DepartmentRetrieveAPIView,
                            TaskListAPIView,
                            TaskCreateAPIView,
                            TaskRetrieveAPIView,
                            ProjectListAPIView,
                            ProjectCreateAPIView,
                            ProjectRetrieveAPIView)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/' , include('rest_framework.urls')),
    path('api/employees/',EmployeeListAPIView.as_view(),name="employees"),
    path('api/employee-create/',EmployeeCreateAPIView.as_view(),name="employee_create"),
    path('api/employee/<int:pk>',EmployeeRetrieveAPIView.as_view(),name="employee"),
    path('api/departments/',DepartmentListAPIView.as_view(),name="departments"),
    path('api/department-create/',DepartmentCreateAPIView.as_view(),name="department_create"),
    path('api/department/<int:pk>',DepartmentRetrieveAPIView.as_view(),name="department"),
    path('api/projects/',ProjectListAPIView.as_view(),name="projects"),
    path('api/project-create/',ProjectCreateAPIView.as_view(),name="project_create"),
    path('api/project/<int:pk>',ProjectRetrieveAPIView.as_view(),name="project"),
    path('api/tasks/',TaskListAPIView.as_view(),name="tasks"),
    path('api/task-create/',TaskCreateAPIView.as_view(),name="task_create"),
    path('api/task/<int:pk>',TaskRetrieveAPIView.as_view(),name="task"),
]
