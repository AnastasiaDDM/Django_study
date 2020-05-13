# from django import forms
# from django.core.exceptions import ValidationError
# from feedback.models import *
# import re
# import dbl
# from feedback.forms import *

# def clean_name(self):
#     name = self.cleaned_data['name']
#     dbl.log("ddddddddd !!!!")
#     dbl.log("dd  "+str(name))
#     # Проверка валидности значения имени
#     if re.match(r'[A-zА-я]+', name) is None:

#         dbl.log("ddddddddd !!!!")
#         # self.add_error(name, "Некорретное имя. Введите имя еще раз или оставьте это поле пустым")

#         raise ValidationError("Некорретное имя. Введите имя еще раз или оставьте это поле пустым")

#     return name




from django import forms
from django.core.exceptions import ValidationError
import re
import dbl

def clean_name(self):
    name = self.cleaned_data['name']
    dbl.log("111 ddddddddd !!!!")
    dbl.log("dd  "+str(name))
    # Проверка валидности значения имени
    if re.match(r'^[A-zА-я]+\s?[A-zА-я]*\s?[A-zА-я]*$', name) is None:

        dbl.log("222 ddddddddd !!!!")
        # self.add_error(name, "Некорретное имя. Введите имя еще раз или оставьте это поле пустым")

        raise ValidationError("Некорретное имя. Введите имя еще раз или оставьте это поле пустым")

    return name


def clean_phone(self):
    phone = self.cleaned_data['phone']
    dbl.log("111 ddddddddd !!!!")
    dbl.log("dd  "+str(phone))
    # Проверка валидности значения имени
    dbl.log("dd телефон "+str(re.match(r'^\+?[78][-\(]?\d{3}\)?-?\d{3}-?\d{2}-?\d{2}$', phone)))
    if re.match(r'^\+?\s?[78]\s?[-\(]?\d{3}\)?\s?-?\s?\d{3}\s?-?\s?\d{2}\s?-?\s?\d{2}$', phone) is None:

        dbl.log("телефон")

        raise ValidationError("Некорретный номер телефона. Попробуйте еще раз")

    return phone


    