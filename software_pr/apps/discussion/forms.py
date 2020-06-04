from django import forms
from django.core.exceptions import ValidationError
import re
# from review.models import Review
import dbl
# Импорт общего приложения 
import util.forms

# Форма для добавления обсуждения или комментария
class Discussion_CommentForm(forms.Form):


    name = forms.CharField(max_length = 250, required=False)
    email_phone = forms.CharField(max_length = 250)
    content = forms.CharField()


    #  Ф-ии проверки валидности полей
    def clean_name(self):

        if self.cleaned_data['name'] is not None:

            return util.forms.clean_name(self)

    def clean_email_phone(self):

        return util.forms.clean_email_phone(self)



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



