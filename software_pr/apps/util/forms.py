from django import forms
from django.core.exceptions import ValidationError
from feedback.models import *
import re
import dbl
from feedback.forms import *

def clean_name(self):
    name = self.cleaned_data['name']
    dbl.log("ddddddddd !!!!")
    dbl.log("dd  "+str(name))
    # Проверка валидности значения имени
    if re.match(r'[A-zА-я]+', name) is None:

        dbl.log("ddddddddd !!!!")
        # self.add_error(name, "Некорретное имя. Введите имя еще раз или оставьте это поле пустым")

        raise ValidationError("Некорретное имя. Введите имя еще раз или оставьте это поле пустым")

    return name