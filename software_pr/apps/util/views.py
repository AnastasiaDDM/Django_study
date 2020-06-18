from django.shortcuts import render
from django.template.loader import render_to_string
from django.conf import settings
from datetime import timedelta, datetime
from django.core.paginator import *
import dbl


# Ф-ия присоединения куки к ответу
def wrap_cookie(response, cookie = {}):
    if 'key' in cookie.keys() :

        # Значение expires по-умолчанию - через 10 лет
        expires = datetime.now() + timedelta(days=3650)

        if 'expires' in cookie.keys():
            expires = cookie['expires']
        response.set_cookie(cookie['key'], cookie['value'], expires= expires, domain=settings.SESSION_COOKIE_DOMAIN, secure=settings.SESSION_COOKIE_SECURE or None)
    return response



def sort_show_by( list_obj, sort_param, count, page):
    # sorting articles by date and rating with ajax
    # data = {}
    dbl.log("111")
    # if request.is_ajax():
    dbl.log("22")
    # dbl.log("22  " + str(request))
    # dbl.log("22  " + str(soft_list))
    for soft in list_obj:
        dbl.log("88  " + str(soft))

    # sort_param = request.GET.get('sortid')
    dbl.log("99 "+str(sort_param))
    # if sort_param in ('create_date', '-create_date', 'rate', '-rate'):
    if sort_param:
        list_obj = list_obj.order_by(sort_param)
        dbl.log("000")
    # data['result'] = render_block_software(request, soft_list)
    # dbl.log("22  " + str(data))
    # return JsonResponse(data)
    dbl.log("33")
    # return HttpResponse(json.dumps(data), content_type='application/json')
    # return super().get(request, *args, **kwargs)



    paginator = Paginator( list_obj, count )


    
    try:
        list_obj = paginator.page(page)
    except(EmptyPage, InvalidPage):
        list_obj = paginator.page(paginator.num_pages) 

    return list_obj