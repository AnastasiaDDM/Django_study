from django import forms
from django.core.exceptions import ValidationError
import re
from feedback.models import Feedback
import dbl
# Импорт общего приложения 
import util.forms

class FeedbackForm(forms.ModelForm):
    class Meta:
        # Описание используемой модели и полей на форме, а также их атрибутов
        model = Feedback
        fields = ['comment', 'phone', 'name']
 
        widgets = {
            'name': forms.TextInput(attrs={'maxlength' : 100, 'id' : 'name'}),
            'phone': forms.TextInput(attrs={'required':True, 'id' : 'phone','type':'tel', 'maxlength' : 25}),
            'comment': forms.Textarea(attrs={'rows':5, 'id' : 'comment'}),
        }
        # {{form.name}}, {{form.phone}} -  таким будет обращение к этим полям из шаблона,
        # {{ form.errors.name }} - а это обращение к ошибкам, генерируемым методами clean_...

    #  Ф-ии проверки валидности полей
    def clean_name(self):

        if self.cleaned_data['name'] is not None:

            return util.forms.clean_name(self)

    def clean_phone(self):

        return util.forms.clean_phone(self)


