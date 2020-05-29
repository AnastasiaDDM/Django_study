from django import forms
from django.core.exceptions import ValidationError
import datetime
from datetime import date
import re
import dbl

#  Общие ф-ии проверки валидности полей
def clean_name(self):
    name = self.cleaned_data['name']
    # Проверка валидности значения имени
    if re.match(r'^[A-zА-я]+\s?[A-zА-я]*\s?[A-zА-я]*$', name) is None:
        raise ValidationError("Некорретное имя. Введите имя еще раз или оставьте это поле пустым")

    return name

def clean_surname(self):
    surname = self.cleaned_data['surname']
    # Проверка валидности значения имени
    if re.match(r'^[A-zА-я]+\s?[A-zА-я]*\s?[A-zА-я]*$', surname) is None:
        raise ValidationError("Некорретная фамилия. Введите имя еще раз или оставьте это поле пустым")

    return surname

def clean_patronymic(self):
    patronymic = self.cleaned_data['patronymic']
    # Проверка валидности значения имени
    if re.match(r'^[A-zА-я]+\s?[A-zА-я]*\s?[A-zА-я]*$', patronymic) is None:
        raise ValidationError("Некорретное отчество. Введите имя еще раз или оставьте это поле пустым")

    return patronymic

def clean_date_of_birth(self):
    date_of_birth = self.cleaned_data['date_of_birth']
    # Проверка валидности значения имени
    # if re.match(r'^[A-zА-я]+\s?[A-zА-я]*\s?[A-zА-я]*$', patronymic) is None:
    #     raise ValidationError("Некорретное отчество. Введите имя еще раз или оставьте это поле пустым")
    if re.match(r'^\d{4}-\d{2}-\d{2}$', str(date_of_birth)) is None:
        raise ValidationError("Неверный тип даты")

    dbl.log(str(date_of_birth))
    years = 10
    days_per_year = 365.24
    dbl.log(str(datetime.date.today() - datetime.timedelta(days=(years*days_per_year))))
    if date_of_birth >= datetime.date.today() - datetime.timedelta(days=(years*days_per_year)):
        raise ValidationError("Кажется выбрана нереальная дата рождения, просим вас поменять значение на реальное")

    return date_of_birth


def clean_phone(self):
    phone = self.cleaned_data['phone']
    # Проверка валидности значения номера телефона
    if re.match(r'^\+?\s?[78]\s?[-\(]?\d{3}\)?\s?-?\s?\d{3}\s?-?\s?\d{2}\s?-?\s?\d{2}$', phone) is None:
        raise ValidationError("Некорретный номер телефона. Попробуйте еще раз")

    return phone

def clean_phone_by_value(phone):
    # phone = self.cleaned_data['phone']
    # Проверка валидности значения номера телефона
    if re.match(r'^\+?\s?[78]\s?[-\(]?\d{3}\)?\s?-?\s?\d{3}\s?-?\s?\d{2}\s?-?\s?\d{2}$', phone) is None:
        raise ValidationError("Некорретный номер телефона. Попробуйте еще раз")
    return phone

def clean_email(self):
    email = self.cleaned_data['email']
    # Проверка валидности значения номера телефона
    if re.match(r'^([a-z0-9_-]+\.)*[a-z0-9_-]+@[a-z0-9_-]+(\.[a-z0-9_-]+)*\.[a-z]{2,6}$', str(email)) is None:
        raise ValidationError("Некорретный адрес электронной почты. Попробуйте еще раз")

    return email

def clean_email_phone(self):
    ephone = self.cleaned_data['email_phone']
    dbl.log(str('клин'))
    # Проверка валидности значения номера телефона
    if (re.match(r'^\+?\s?[78]\s?[-\(]?\d{3}\)?\s?-?\s?\d{3}\s?-?\s?\d{2}\s?-?\s?\d{2}$', str(ephone)) is None) and (re.match(r'^([a-z0-9_-]+\.)*[a-z0-9_-]+@[a-z0-9_-]+(\.[a-z0-9_-]+)*\.[a-z]{2,6}$', str(ephone)) is None):
        dbl.log(str('данные ошибочны!!'))
        raise ValidationError("Некорретное значение. Попробуйте еще раз")

    return ephone


def clean_date(date):

    # if re.match(r'^\d{1,2}\.\d{2}\.\d{4}$', str(date_from)) is None:
    if re.match(r'^\d{4}-\d{2}-\d{2}$', str(date)) is None:
        raise ValidationError("Неверный тип даты")

    return date