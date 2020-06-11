from django.shortcuts import render
import dbl
from django.db import models
from software.models import Software, Tag
from review.models import Review
from software.views import render_horizontal_widgets

def index(request):

    # Блок новинок
    new_soft = Software.get_new()
    dbl.log("0")

    # Ф-ия составления html кода горихонтальных виджетов
    block_new_soft = render_horizontal_widgets(new_soft, id_widget="new_software")

    # Блок видов ПО
    site_soft = Software.software_list_by_type(cl_val=2)
    block_site_soft = render_horizontal_widgets(site_soft, id_widget="site_software", display_type="style=display:none;", widget_shell=False,
    show_more="/softwares/?classification_1_value_2=2")

    desktop_soft = Software.software_list_by_type(cl_val=1)
    block_desktop_soft = render_horizontal_widgets(desktop_soft, id_widget="desktop_software", widget_shell=False,
    show_more="/softwares/?classification_1_value_1=1")

    mobile_soft = Software.software_list_by_type(cl_val=3)
    block_mobile_soft = render_horizontal_widgets(mobile_soft, id_widget="mobile_software", display_type="style=display:none;", widget_shell=False,
    show_more="/softwares/?classification_1_value_3=3")

    # Блок отзывов
    list_review = Review.objects.all().filter(date_of_delete=None, visibility=True, star__gte=4).order_by('-date')[:3]

    # Блок тегов
    list_tag = Tag.objects.all().filter(date_of_delete=None, visibility=True).order_by('name')

    return render(request, 'main/index.html', {'block_new_soft':block_new_soft, 'block_site_soft':block_site_soft,
    'block_desktop_soft':block_desktop_soft, 'block_mobile_soft':block_mobile_soft, 'list_review':list_review, 'list_tag':list_tag})