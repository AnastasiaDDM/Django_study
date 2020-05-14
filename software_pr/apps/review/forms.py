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
        fields = ['content', 'comment',  'name']
 
        widgets = {
            'name': forms.TextInput(attrs={'maxlength' : 100, 'id' : 'name'}),
            # 'ephone': forms.TextInput(attrs={'required':True, 'id' : 'ephone','type':'tel', 'maxlength' : 25}),
            'content': forms.Textarea(attrs={'rows':5, 'id' : 'comment'}),
            'comment': forms.Textarea(attrs={'rows':5, 'id' : 'comment'}),
            # 'kind': forms.TextInput(attrs={'required':True, 'id' : 'phone','type':'tel', 'maxlength' : 25}),
        }
        # {{form.name}}, {{form.phone}} -  таким будет обращение к этим полям из шаблона,
        # {{ form.errors.name }} - а это обращение к ошибкам, генерируемым методами clean_...

    #  Ф-ии проверки валидности полей
    def clean_name(self):

        if self.cleaned_data['name'] is not None:

            return util.forms.clean_name(self)

    # def clean_ephone(self):

    #     return util.forms.clean_ephone(self)


