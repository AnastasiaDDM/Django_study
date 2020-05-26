from django.shortcuts import render, redirect
from user.models import CustomUser
from user.authentication import get_user_by_email_phone
import dbl
import re


def personal_data(request):
    if request.user.is_authenticated:
        dbl.log(str(request.user))
        return render(request, 'user/personal_data.html', {})

def personal_data_edit(request):
    if request.user.is_authenticated:
        dbl.log(str(request.user))
        return render(request, 'user/personal_data_edit.html', {})

