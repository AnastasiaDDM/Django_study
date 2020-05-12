from django import forms
from django.core.exceptions import ValidationError
from feedback.models import *
import re
import dbl

class FeedbackForm(forms.ModelForm):
    class Meta:
        model = Feedback
        fields = ['comment', 'phone', 'name']

        widgets = {
            'comment': forms.Textarea(attrs={}),
            'phone': forms.TextInput(attrs={'required':True}),
            'name': forms.TextInput(attrs={}),
        }

        # def clean_phone(self):
        #     email = self.cleaned_data['phone']
        #     if User.objects.filter(email=email).exists():
        #         raise ValidationError("Email already exists")
        #     return email

        def clean_name(self):
            name = self.cleaned_data['name']
            dbl.log("ddddddddd !!!!")
            # Проверка валидности значения имени
            if re.match(r'[A-zА-я]+', name) is False:

                dbl.log("ddddddddd !!!!")

                raise ValidationError("Некорретное имя. Введите имя еще раз или оставьте это поле пустым")

            return name


