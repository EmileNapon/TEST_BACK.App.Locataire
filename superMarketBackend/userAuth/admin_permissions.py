from rest_framework import permissions
    
class IsCitoyen(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.type_user == 'citoyen' 
    

