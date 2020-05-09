from django import template

register = template.Library()


@register.filter(name='get_value_for_dict')

def get_true_for_dict(dictionary, value):
    if value in dictionary.values():
        return True
    else:
        return False

def get_value_for_dict(dictionary, key):
    return dictionary.get(key)

