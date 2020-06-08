from django import forms
from django.core.exceptions import ValidationError
import re
from order.models import Order
import dbl
# Импорт общего приложения 
import util.forms

# # Форма для добавления отзыва
# class ReviewForm(forms.ModelForm):
#     class Meta:
#         # Описание используемой модели и полей на форме, а также их атрибутов
#         model = Review
#         fields = ['content', 'comment', 'email_phone', 'name', 'star', 'software']

#         widgets = {
#             'name': forms.TextInput(attrs={'maxlength' : 100, 'id' : 'name'}),
#             'email_phone': forms.TextInput(attrs={'required':True, 'id' : 'ephone', 'maxlength' : 25}),
#             'content': forms.Textarea(attrs={'rows':5, 'id' : 'content'}),
#             'comment': forms.Textarea(attrs={'rows':5, 'id' : 'comment'}),
#             'star': forms.TextInput(attrs={'required':True,'type':'radio'}),
#         }
#         # {{form.name}}, {{form.phone}} -  таким будет обращение к этим полям из шаблона,
#         # {{ form.errors.name }} - а это обращение к ошибкам, генерируемым методами clean_...

#     #  Ф-ии проверки валидности полей
#     def clean_name(self):

#         if self.cleaned_data['name'] is not None:

#             return util.forms.clean_name(self)

#     def clean_email_phone(self):

#         return util.forms.clean_email_phone(self)

#     def clean_star(self):
#         star = self.cleaned_data['star']
#         dbl.log('звезда !'+str(star))
#         # Проверка валидности значения рейтинга
#         if star == "":
#             dbl.log('звездыыыыы'+str(star))
#             raise ValidationError("Пожалуйста поставьте оценку")

#         return star


# Форма элементов для поиска заказов
class Search_OrderForm(forms.Form):

    date_type = forms.CharField(required=False)
    date_from = forms.DateField(required=False)
    date_to = forms.DateField(required=False)
    month = forms.CharField(required=False)
    status_order = forms.CharField(required=False)
    type_order = forms.CharField(required=False)
    type_soft = forms.CharField(required=False)
    number = forms.CharField(required=False)
    name = forms.CharField(required=False)
    unread_messages = forms.BooleanField(required=False)


    #  Ф-ии проверки валидности полей
    def clean_date_from(self):
        
        date_from = self.cleaned_data['date_from']
        if date_from is not None:

            return util.forms.clean_date(date_from)

    def clean_date_to(self):
        
        date_to = self.cleaned_data['date_to']
        if date_to is not None:

            return util.forms.clean_date(date_to)

    def clean_number(self):
        
        number = self.cleaned_data['number']

        if number is not None and str(number) != "":

            return util.forms.clean_isdigit(number)