from django.contrib.auth.backends import BaseBackend
from django.core.exceptions import PermissionDenied
from django.contrib.auth import get_user_model
from django.contrib import messages


User = get_user_model()


class MyAuthenticationBackend(BaseBackend):
    
    
    def authenticate(self, request, username=None, password=None, email=None):

        try:
            user = User.objects.get(username=username, email=email)
            
            if user.check_password(password):
                return user
        except User.DoesNotExist:
            messages.error(request, "User with these username and login does not exist.")
            raise PermissionDenied("User does not exist")
        
        return None
    
    
    def get_user(self, user_pk):

        try:
            return User.objects.get(pk=user_pk)
        except User.DoesNotExist:
            return None