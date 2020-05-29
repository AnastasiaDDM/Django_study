from django import forms
from django.core.exceptions import ValidationError
import re
from user.models import CustomUser
import dbl
# Импорт общего приложения 
import util.forms


# Форма для редактирования персональных данных
class PersonalForm(forms.Form):

    name = forms.CharField(max_length = 250, required=False)
    surname = forms.CharField(max_length = 250, required=False)
    patronymic = forms.CharField(max_length = 250, required=False)
    email = forms.CharField(max_length = 250, required=False)
    phone = forms.CharField(max_length = 250, required=False)
    phone_second = forms.CharField(max_length = 250, required=False)
    social = forms.CharField(max_length = 900, required=False)
    date_of_birth = forms.DateField(required=False)



    # class Meta:
        # Описание используемой модели и полей на форме, а также их атрибутов
        # model = CustomUser
        # fields = ['email', 'name', 'surname', 'patronymic',  'phone', 'phone_second', 'date_of_birth', 'social']
 
        # widgets = {
        #     'name': forms.TextInput(attrs={'maxlength' : 100, 'id' : 'name'}),
        #     'surname': forms.TextInput(attrs={'maxlength' : 100, 'id' : 'surname'}),
        #     'patronymic': forms.TextInput(attrs={'maxlength' : 100, 'id' : 'patronymic'}),
        #     'email': forms.TextInput(attrs={'maxlength' : 50}),
        #     'phone': forms.TextInput(attrs={'maxlength' : 25}),
        # }
        # {{form.name}}, {{form.phone}} -  таким будет обращение к этим полям из шаблона,
        # {{ form.errors.name }} - а это обращение к ошибкам, генерируемым методами clean_...

    #  Ф-ии проверки валидности полей
    def clean_name(self):
        dbl.log("rrr")
        dbl.log(str(self.cleaned_data['name']))

        if len(self.cleaned_data['name']) >0:
            dbl.log("aaa")

            return util.forms.clean_name(self)
        else:

            return self.cleaned_data['name']


    def clean_surname(self):
        dbl.log("rrr")
        dbl.log(str(self.cleaned_data['surname']))

        if len(self.cleaned_data['surname']) >0:
            dbl.log("aaa")

            return util.forms.clean_surname(self)
        else:

            return self.cleaned_data['surname']

    def clean_patronymic(self):
        dbl.log("rrr")
        dbl.log(str(self.cleaned_data['patronymic']))

        if len(self.cleaned_data['patronymic']) >0:
            dbl.log("aaa")

            return util.forms.clean_patronymic(self)
        else:

            return self.cleaned_data['patronymic']

    def clean_date_of_birth(self):
        dbl.log("rrr")
        dbl.log(str(self.cleaned_data['date_of_birth']))

        if self.cleaned_data['date_of_birth'] is not None:
            dbl.log("aaa")

            return util.forms.clean_date_of_birth(self)
        else:
            return self.cleaned_data['date_of_birth']

    def clean_phone(self):
        phone = self.cleaned_data['phone']
        if len(phone) >0:
            return util.forms.clean_phone_by_value(phone)
        else:
            return phone

    def clean_phone_second(self):
        phone = self.cleaned_data['phone_second']
        if len(phone) >0:
            return util.forms.clean_phone_by_value(phone)
        else:
            return phone
            

    def clean_email(self):
        dbl.log(str(self.cleaned_data['email']))
        
        if self.cleaned_data['email'] is not None:
            dbl.log("aaa")

        return util.forms.clean_email(self)



# # Форма для добавления отзыва
# class PersonalForm(forms.ModelForm):
#     class Meta:
#         # Описание используемой модели и полей на форме, а также их атрибутов
#         model = CustomUser
#         fields = ['email', 'name', 'surname', 'patronymic',  'phone', 'phone_second', 'date_of_birth', 'social']
 
#         widgets = {
#             'name': forms.TextInput(attrs={'maxlength' : 100, 'id' : 'name'}),
#             'surname': forms.TextInput(attrs={'maxlength' : 100, 'id' : 'surname'}),
#             'patronymic': forms.TextInput(attrs={'maxlength' : 100, 'id' : 'patronymic'}),
#             'email': forms.TextInput(attrs={'maxlength' : 50}),
#             'phone': forms.TextInput(attrs={'maxlength' : 25}),
#         }
#         # {{form.name}}, {{form.phone}} -  таким будет обращение к этим полям из шаблона,
#         # {{ form.errors.name }} - а это обращение к ошибкам, генерируемым методами clean_...

#     #  Ф-ии проверки валидности полей
#     def clean_name(self):

#         if self.cleaned_data['name'] is not None:

#             return util.forms.clean_name(self)

#     def clean_email(self):

#         return util.forms.clean_email(self)

    # def clean_star(self):
    #     star = self.cleaned_data['star']
    #     dbl.log('звезда !'+str(star))
    #     # Проверка валидности значения рейтинга
    #     if star == "":
    #         dbl.log('звездыыыыы'+str(star))
    #         raise ValidationError("Пожалуйста поставьте оценку")

    #     return star


# # Форма элементов для поиска отзывов
# class Search_ReviewForm(forms.Form):

#     rating_from = forms.CharField(max_length=5, required=False)
#     rating_to = forms.CharField(max_length=5, required=False)
#     date_from = forms.DateField(required=False)
#     date_to = forms.DateField(required=False)
#     review_type = forms.CharField(required=False)

#     #  Ф-ии проверки валидности полей
#     def clean_date_from(self):
        
#         date_from = self.cleaned_data['date_from']
#         dbl.log('звездыыыыы'+str(date_from))
#         if date_from is not None:

#             return util.forms.clean_date(date_from)


#             # # if re.match(r'^\d{1,2}\.\d{2}\.\d{4}$', str(date_from)) is None:
#             # if re.match(r'^\d{4}-\d{2}-\d{2}$', str(date_from)) is None:
#             #     raise ValidationError("Некорретное имя. Введите имя еще раз или оставьте это поле пустым")



