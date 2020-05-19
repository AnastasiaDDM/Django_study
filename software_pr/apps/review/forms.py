from django import forms
from django.core.exceptions import ValidationError
import re
from review.models import Review
import dbl
# Импорт общего приложения 
import util.forms

class ReviewForm(forms.ModelForm):
    class Meta:
        # Описание используемой модели и полей на форме, а также их атрибутов
        model = Review
        fields = ['content', 'comment', 'email_phone', 'name', 'star', 'software']
 
        widgets = {
            'name': forms.TextInput(attrs={'maxlength' : 100, 'id' : 'name'}),
            'email_phone': forms.TextInput(attrs={'required':True, 'id' : 'ephone', 'maxlength' : 25}),
            'content': forms.Textarea(attrs={'rows':5, 'id' : 'content'}),
            'comment': forms.Textarea(attrs={'rows':5, 'id' : 'comment'}),
            # 'software': forms.TextInput(attrs={'maxlength' : 200, 'id' : 'software'}),
            'star': forms.TextInput(attrs={'required':True,'type':'radio'}),
            # 'kind': forms.TextInput(attrs={'required':True, 'id' : 'phone','type':'tel', 'maxlength' : 25}),
        }
        # {{form.name}}, {{form.phone}} -  таким будет обращение к этим полям из шаблона,
        # {{ form.errors.name }} - а это обращение к ошибкам, генерируемым методами clean_...

    #  Ф-ии проверки валидности полей
    def clean_name(self):

        if self.cleaned_data['name'] is not None:

            return util.forms.clean_name(self)

    def clean_email_phone(self):

        return util.forms.clean_email_phone(self)

    def clean_star(self):
        star = self.cleaned_data['star']
        dbl.log('звезда !'+str(star))
        # Проверка валидности значения рейтинга
        if star == "":
            dbl.log('звездыыыыы'+str(star))
            raise ValidationError("Пожалуйста поставьте оценку")

        return star



# class Search_ReviewForm(forms.ModelForm):
#     class Meta:
#         # Описание используемой модели и полей на форме, а также их атрибутов
#         model = Review
#         fields = ['rating_from', 'rating_to', 'date_from', 'date_to', 'review_type']

