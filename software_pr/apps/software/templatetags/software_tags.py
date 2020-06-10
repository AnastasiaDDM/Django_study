from django import template
from django.db import models
from software.models import *
import dbl


register = template.Library()


@register.filter(name='get_true_for_dict')
def get_true_for_dict(dictionary, value):
    if value in dictionary.values():
        return True
    else:
        return False


@register.filter(name='is_identical_for_dict')
def is_identical_for_dict(dictionary, value):

    val_obj = Classification_Value.objects.get( value = value )
    # dbl.log("Андрей ---------")
    # dbl.log(str(val_obj)+"ddddd "+ str(val_obj.id))
    # dbl.log("словарь "+str(dictionary))
    # dbl.log("1111  "+str(dictionary.values()))
    for val in dictionary.values():

        # dbl.log("бебебе  "+str(val))

        if str(val_obj.id) == str(val):

            # dbl.log("дваааааа "+str(val_obj.id))
            return True
            
    return False


@register.filter(name='get_value_for_dict')
def get_value_for_dict(dictionary, key):
    try:
        return dictionary.get(key)
    except:
        return None



# Ф-ия проверки является ли данное ПО избранным у конкретного клиента
@register.filter(name='is_favourite')
def is_favourite(self, client):
    try: 
        return Favourite.objects.filter(software=self.id, client=client.id )
    except:
        return None


# Ф-ия получения даты добавления избранного
@register.filter(name='get_date_joined')
def get_date_joined(self, client):
    try:
        if client:
            favourite = Favourite.objects.get(software=self.id, client=client.id) 
            return favourite.date_joined
        return None
    except:
        return None

        