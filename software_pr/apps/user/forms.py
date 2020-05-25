from django import forms
from django.core.exceptions import ValidationError
import re
from review.models import Review
import dbl
# Импорт общего приложения 
import util.forms
from user.models import CustomUser
# from django.contrib.auth.models import CustomUser
from django.contrib.auth.forms import UserCreationForm


class LoginForm(forms.Form):

#     class Meta:
#         model = CustomUser
#         fields = ('email', 'password')



# class LoginForm(UserCreationForm):

    # class Meta:
    #     # model = CustomUser
    #     fields = ('email', 'password')
        # fields = ('password')

        
    email_phone = forms.CharField(max_length = 250)
    password = forms.CharField(max_length = 50)


        # widgets = {
        #     # 'phone': forms.TextInput(attrs={'required':True, 'id' : 'phone', 'maxlength' : 25}),
        #     'email': forms.TextInput(attrs={ 'id' : 'email', 'maxlength' : 25, 'autofocus':True}),
        #     'password': forms.TextInput(attrs={'type':'password', 'id' : 'password',}),
        # }
        # {{form.name}}, {{form.phone}} -  таким будет обращение к этим полям из шаблона,
        # {{ form.errors.name }} - а это обращение к ошибкам, генерируемым методами clean_...

    #  Ф-ии проверки валидности полей
    def clean_email_phone(self):

        return util.forms.clean_email_phone(self)




class RegisterForm(forms.Form):
#     '''Simple login form'''
#     class Meta:
#         model = CustomUser
#         fields = ('email', 'password')

    email_phone = forms.CharField(max_length = 250)
    password = forms.CharField(max_length = 50)

    #  Ф-ии проверки валидности полей
    def clean_email_phone(self):

        return util.forms.clean_email_phone(self)



# class LoginForm(UserCreationForm):
    # '''Simple login form'''
    # class Meta:
    #     model = CustomUser
    #     fields = ('email', 'password')
        # fields = ('password')


        # widgets = {
        #     # 'phone': forms.TextInput(attrs={'required':True, 'id' : 'phone', 'maxlength' : 25}),
        #     'email': forms.TextInput(attrs={ 'id' : 'email', 'maxlength' : 25, 'autofocus':True}),
        #     'password': forms.TextInput(attrs={'type':'password', 'id' : 'password',}),
        # }
        # {{form.name}}, {{form.phone}} -  таким будет обращение к этим полям из шаблона,
        # {{ form.errors.name }} - а это обращение к ошибкам, генерируемым методами clean_...
