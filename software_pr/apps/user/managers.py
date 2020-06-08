from django.contrib.auth.base_user import BaseUserManager
# from user.models import CustomUser
import dbl
from django.db.models import Q


class CustomUserManager(BaseUserManager):
    use_in_migrations = True

    # def _create_user(self, email, password, **extra_fields):

    #     if not email:
    #         raise ValueError('Введите email')
    #     email = self.normalize_email(email)
    #     user = self.model(email=email, **extra_fields)
    #     user.set_password(password)
    #     user.save(using=self._db)
    #     return user



    def _create_user(self, email=None, phone=None, password=None, **extra_fields):

        # if not email:
        #     raise ValueError('Введите email')
        if email:
            email = self.normalize_email(email)
            # extra_fields.setdefault('phone', No)
            user = self.model(email=email, **extra_fields)
        else:
            user = self.model(phone=phone, **extra_fields)
        dbl.log('манагер '+str(email)+str(phone)+str(password))
        # user = self.model(email=email, phone=phone, **extra_fields)
        # dbl.log(str(user))
        user.set_password(password)
        user.save()
        return user


    def create_user(self, email=None, phone=None, password=None, session=None, max_age=None, **extra_fields):

        if session:
            dbl.log('сесиия ' +str(session)  )
            dbl.log("время "+str(max_age))
            extra_fields.setdefault('is_superuser', False)
            user = self.model(guest_session=session, max_age=max_age)
            # user = Cus
            # user.guest_session = session
            # user.max_age =max_age
            user.save()
            dbl.log('сесиия юзер до' )
            # dbl.log('сесиия юзер' +str(user) )
            dbl.log('сесиия юзер после' )
            return user

        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email=email, phone=phone, password=password, **extra_fields)



    # def _create_user(self, email=None, phone=None, password=None, guest_session=None, max_age=None, **extra_fields):

    #     # if not email:
    #     #     raise ValueError('Введите email')
    #     if email:
    #         email = self.normalize_email(email)
    #         # extra_fields.setdefault('phone', No)
    #         user = self.model(email=email, **extra_fields)
    #     if phone:
    #         user = self.model(phone=phone, **extra_fields)

    #     if guest_session:
    #         dbl.log('сесиия ' +str(guest_session)  )
    #         dbl.log("время "+str(max_age))
    #         # extra_fields.setdefault('is_superuser', False)
    #         user = self.model(guest_session=guest_session, max_age=max_age, **extra_fields)
    #         # user = Cus
    #         # user.guest_session = session
    #         # user.max_age =max_age
    #         # user.save()
    #         dbl.log('сесиия юзер' +str(user) )
    #         # return user

    #     dbl.log('манагер '+str(email)+str(phone)+str(password))
    #     # user = self.model(email=email, phone=phone, **extra_fields)
    #     # dbl.log(str(user))
    #     user.set_password(password)
    #     user.save()
    #     return user


    # def create_user(self, email=None, phone=None, password=None, session=None, max_age=None, **extra_fields):

    #     # if session:
    #     #     dbl.log('сесиия ' +str(session)  )
    #     #     dbl.log("время "+str(max_age))
    #     #     extra_fields.setdefault('is_superuser', False)
    #     #     user = self.model(guest_session=session, max_age=max_age)
    #     #     # user = Cus
    #     #     user.guest_session = session
    #     #     user.max_age =max_age
    #     #     user.save()
    #     #     dbl.log('сесиия юзер' +str(user) )
    #     #     return user

    #     extra_fields.setdefault('is_superuser', False)
    #     return self._create_user(email=email, phone=phone, password=password, guest_session=session, max_age=max_age, **extra_fields)




    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(email, password, **extra_fields)

  
# def get_user_by_email_phone(email_or_phone):
#     try:
#         dbl.log('манагер юзер ')
#         dbl.log('манагер юзер '+str(CustomUser.objects.get(Q(email=email_or_phone) | Q(phone=email_or_phone))))
#         return CustomUser.objects.get(Q(email=email_or_phone) | Q(phone=email_or_phone))
#     except :
#         return None
