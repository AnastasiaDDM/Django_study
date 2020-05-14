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

def clean_ephone(self):
    phone = self.cleaned_data['ephone']
    # Проверка валидности значения номера телефона
    if re.match(r'^\+?\s?[78]\s?[-\(]?\d{3}\)?\s?-?\s?\d{3}\s?-?\s?\d{2}\s?-?\s?\d{2}$', phone) is None:
        raise ValidationError("Некорретный номер телефона. Попробуйте еще раз")

    return phone

        # def clean_phone(self):
        #     email = self.cleaned_data['phone']
        #     if User.objects.filter(email=email).exists():
        #         raise ValidationError("Email already exists")
        #     return email
    