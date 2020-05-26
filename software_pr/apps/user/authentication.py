from user.models import CustomUser
# from django.contrib.auth.models import CustomUser
from django.contrib.auth.models import User
from django.db.models import Q
import dbl

class Email_PhoneAuthBackend:

    def authenticate(self, request, email_or_phone=None, password=None):
        dbl.log('авт вход')
        try:
            dbl.log('авт  номер '+str(email_or_phone)+str(password))
            user = CustomUser.objects.get(Q(email=email_or_phone) | Q(phone=email_or_phone))
            # user = CustomUser.objects.get(email=str(email_or_phone))
            # user = CustomUser.objects.get(kind='ADM')
            # user = CustomUser.objects.get(surname='Дмитриева')
            dbl.log('авт Эавввльавлтввтаоватватвососчс')
            dbl.log('авт юзер '+str(user))
            pwd_valid = user.check_password(password)
            if pwd_valid:
                dbl.log('авт хороший пароль')            
                return user
            if str(user)=='':
                return None
        except :
            dbl.log('авт ошибочка в поиске') 
            return None

    def get_user(self, user_id):
        try:
            return CustomUser.objects.get(pk=user_id)
        except :
            return None

    # @staticmethod
    # def get_user_by_email_phone(self, email_or_phone):
    #     try:
    #         return CustomUser.objects.get(Q(email=email_or_phone) | Q(phone=email_or_phone))
    #     except :
    #         return None

  
def get_user_by_email_phone(email_or_phone):
    try:
        dbl.log('манагер юзер ')
        dbl.log('манагер юзер '+str(CustomUser.objects.get(Q(email=email_or_phone) | Q(phone=email_or_phone))))
        return CustomUser.objects.get(Q(email=email_or_phone) | Q(phone=email_or_phone))
    except :
        return None