from rest_framework import permissions
from .models import CustomUser

#es permission ekutvnis administrators
class IsAdministrator(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.role == CustomUser.ADMINISTRATOR
    
class CanDeleteReport(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return request.user.role == CustomUser.COURIER
    
class CanAddReport(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return request.user.role == CustomUser.OFFICE_WORKER

# class IsOfficeWorker(permissions.BasePermission):
#     def has_permission(self, request, view):
#         if request.method in permissions.SAFE_METHODS:
#             return True
        
#         return request.user.is_authenticated and request.user.role == CustomUser.OFFICE_WORKER