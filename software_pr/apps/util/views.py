from django.shortcuts import render
from django.template.loader import render_to_string
from django.conf import settings
from datetime import timedelta, datetime


# Ф-ия присоединения куки к ответу
def wrap_cookie(response, cookie = {}):
    if 'key' in cookie.keys() :

        # Значение expires по-умолчанию - через 10 лет
        expires = datetime.now() + timedelta(days=3650)

        if 'expires' in cookie.keys():
            expires = cookie['expires']
        response.set_cookie(cookie['key'], cookie['value'], expires= expires, domain=settings.SESSION_COOKIE_DOMAIN, secure=settings.SESSION_COOKIE_SECURE or None)
    return response