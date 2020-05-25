from django.contrib.auth.base_user import BaseUserManager
import dbl


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


    def create_user(self, email=None, phone=None, password=None, **extra_fields):
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email=email, phone=phone, password=password, **extra_fields)




    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(email, password, **extra_fields)





# def _create_user(self, email=None, phone=None, password=None, **extra_fields):

#     # if not email:
#     #     raise ValueError('Введите email')
#     email = self.normalize_email(email)
#     user = self.model(email=email, **extra_fields)
#     user.set_password(password)
#     user.save()
#     return user


# def create_user(self, email=None, phone=None, password=None, **extra_fields):
#     extra_fields.setdefault('is_superuser', False)
#     return self._create_user(email=email, phone=phone, password=password, **extra_fields)


