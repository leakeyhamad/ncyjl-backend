from rest_framework.permissions import BasePermission

class IsYouth(BasePermission):
    def has_permission(self, request, view):
        return request.user.role == "youth"

class IsOfficial(BasePermission):
    def has_permission(self, request, view):
        return request.user.role == "official"

class IsSupervisor(BasePermission):
    def has_permission(self, request, view):
        return request.user.role == "supervisor"
