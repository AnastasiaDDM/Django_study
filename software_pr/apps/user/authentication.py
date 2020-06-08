from user.models import CustomUser
# from django.contrib.auth.models import CustomUser
from django.contrib.auth.models import User
from django.db.models import Q
import dbl

class Email_PhoneAuthBackend:

    def authenticate(self, request, email_or_phone=None, password=None):
        try:
            user = CustomUser.objects.get(Q(email=email_or_phone) | Q(phone=email_or_phone))
            pwd_valid = user.check_password(password)
            if pwd_valid:       
                return user
            if str(user)=='':
                return None
        except :
            return None

    def get_user(self, user_id):
        try:
            return CustomUser.objects.get(pk=user_id)
        except :
            return None