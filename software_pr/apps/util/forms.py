from django import forms
from django.core.exceptions import ValidationError
import re
import dbl

#  Общие ф-ии проверки валидности полей
def clean_name(self):
    name = self.cleaned_data['name']
    # Проверка валидности значения имени
    if re.match(r'^[A-zА-я]+\s?[A-zА-я]*\s?[A-zА-я]*$', name) is None:
        raise ValidationError("Некорретное имя. Введите имя еще раз или оставьте это поле пустым")

    return name


def clean_phone(self):
    phone = self.cleaned_data['phone']
    # Проверка валидности значения номера телефона
    if re.match(r'^\+?\s?[78]\s?[-\(]?\d{3}\)?\s?-?\s?\d{3}\s?-?\s?\d{2}\s?-?\s?\d{2}$', phone) is None:
        raise ValidationError("Некорретный номер телефона. Попробуйте еще раз")

    return phone

def clean_email_phone(self):
    ephone = self.cleaned_data['email_phone']
    # Проверка валидности значения номера телефона

    # dbl.log(str(re.match(r'^\+?\s?[78]\s?[-\(]?\d{3}\)?\s?-?\s?\d{3}\s?-?\s?\d{2}\s?-?\s?\d{2}$', str(ephone)) is None))
    # dbl.log(str(re.match(r'^([a-z0-9_-]+\.)*[a-z0-9_-]+@[a-z0-9_-]+(\.[a-z0-9_-]+)*\.[a-z]{2,6}$', str(ephone)) is None))
    if (re.match(r'^\+?\s?[78]\s?[-\(]?\d{3}\)?\s?-?\s?\d{3}\s?-?\s?\d{2}\s?-?\s?\d{2}$', str(ephone)) is None) and (re.match(r'^([a-z0-9_-]+\.)*[a-z0-9_-]+@[a-z0-9_-]+(\.[a-z0-9_-]+)*\.[a-z]{2,6}$', str(ephone)) is None):
        dbl.log(str('dddddddddd'))
        raise ValidationError("Некорретное значение. Попробуйте еще раз")

    return ephone

        # def clean_phone(self):
        #     email = self.cleaned_data['phone']
        #     if User.objects.filter(email=email).exists():
        #         raise ValidationError("Email already exists")
        #     return email
    