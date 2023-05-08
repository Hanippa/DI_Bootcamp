from rest_framework import permissions

class IsDepartmentAdmin(permissions.BasePermission):
    # def has_permission(self, request, view):
    #     if request.user.username == 'dekel':
    #         return True
    #     return False
    def has_permission(self, request, view):
        if not request.user.is_anonymous:
            if request.user.employee_user.department_administrator:
                return True
        return False