from rest_framework import permissions


class GlobalDefaultPermission(permissions.BasePermission):

    def has_permission(self, request, view):
        model_permission_codname = self.__get_model_permission_codename(method=request.method, view=view,)

        if not model_permission_codname:
            return False
                
        return request.user.has_perm(model_permission_codname)
    
    def __get_model_permission_codename(self, method, view):
        try:
            app_label  = view.queryset.model._meta.app_label
            model_name = view.queryset.model._meta.model_name
            action     = self.__get_action_sufix(method)

            return f'{app_label}.{action}_{model_name}'
        except AttributeError:
            return None
    
    def __get_action_sufix(self, method):
        method_actions = {
            'GET': 'view',
            'POST': 'add',
            'PUT': 'change',
            'PATCH': 'change',
            'DELETE': 'delete',
            'OPTIONS': 'view',
            'HEAD': 'view',
        }
        return method_actions.get(method, '')