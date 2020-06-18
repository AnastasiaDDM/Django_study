from django import template
from django.template import loader, Node, Variable
from django.utils.encoding import smart_str
from django.template.defaulttags import url
from django.template import VariableDoesNotExist
import re
import dbl

register = template.Library()

@register.tag
def breadcrumb(parser, token):
    """
    Renders the breadcrumb.
    Examples:
        {% breadcrumb "Title of breadcrumb" url_var %}
        {% breadcrumb context_var  url_var %}
        {% breadcrumb "Just the title" %}
        {% breadcrumb just_context_var %}

    Parameters:
    -First parameter is the title of the crumb,
    -Second (optional) parameter is the url variable to link to, produced by url tag, i.e.:
        {% url person_detail object.id as person_url %}
        then:
        {% breadcrumb person.name person_url %}

    @author Andriy Drozdyuk
    """
    return BreadcrumbNode(token.split_contents()[1:])


@register.tag
def breadcrumb_url(parser, token):
    """
    Same as breadcrumb
    but instead of url context variable takes in all the
    arguments URL tag takes.
        {% breadcrumb "Title of breadcrumb" person_detail person.id %}
        {% breadcrumb person.name person_detail person.id %}
    """

    bits = token.split_contents()
    if len(bits)==2:
        return breadcrumb(parser, token)

    # Extract our extra title parameter
    title = bits.pop(1)
    token.contents = ' '.join(bits)

    url_node = url(parser, token)

    return UrlBreadcrumbNode(title, url_node)


class BreadcrumbNode(Node):
    def __init__(self, vars):
        """
        First var is title, second var is url context variable
        """
        self.vars = list(map(Variable,vars))

    def render(self, context):
        title = self.vars[0].var

        if title.find("'")==-1 and title.find('"')==-1:
            try:
                val = self.vars[0]
                title = val.resolve(context)
            except:
                title = ''

        else:
            title=title.strip("'").strip('"')
            # title=smart_unicode(title)

        url = None

        if len(self.vars)>1:
            val = self.vars[1]
            try:
                url = val.resolve(context)
            except VariableDoesNotExist:
                print ('URL does not exist', val)
                url = None

        return create_crumb(title, url)


class UrlBreadcrumbNode(Node):
    def __init__(self, title, url_node):
        self.title = Variable(title)
        self.url_node = url_node

    def render(self, context):
        title = self.title.var

        if title.find("'")==-1 and title.find('"')==-1:
            try:
                val = self.title
                title = val.resolve(context)
            except:
                title = ''
        else:
            title=title.strip("'").strip('"')
            # title=smart_unicode(title)

        url = self.url_node.render(context)
        return create_crumb(title, url)


def create_crumb(title, url=None):
    """
    Helper function
    """
    # crumb = """<span class="breadcrumbs-arrow">""" \
    #         """<img src="/media/images/arrow.gif" alt="Arrow">""" \
    #         """</span>"""
    crumb = ' ~ '
    if url:
        crumb = "%s<a href='%s'>%s</a>" % (crumb, url, title)
    else:
        # crumb = "%s&nbsp;&nbsp;%s" % (crumb, title)
        crumb = "%s%s" % (crumb, title)

    return crumb



@register.filter(name='comparison_numbers')
def comparison_numbers(first_num, second_num):
    if str(first_num).isdigit() and str(second_num).isdigit():
        if int(first_num) == int(second_num):
            return True

    return False


@register.filter(name='more_than_numbers')
def more_than_numbers(first_num, second_num):
    if str(first_num).isdigit() and str(second_num).isdigit():
        if int(first_num) >= int(second_num):
            return True

    return False


@register.filter(name='reverse_for_star')
def reverse_for_star(num):
    if str(num).isdigit():

        return 6 - int(num)

    return 0


@register.filter(name='get_value_in_dict')
def get_value_in_dict(dictionary, key):
    try:
        return dictionary.get(key)

    except:
        return None

@register.filter(name='subtraction')
def subtraction(first_num, second_num):
    try:
        return float(first_num) - float(second_num)
    except:
        return None


@register.filter(name='list_cross_section')
def list_cross_section(list, start_index=0):
    return list[start_index:]
        

@register.filter(name='return_str')
def return_str(param):
    return str(param)
        

@register.filter(name='is_active')
def is_active(request, name=''):
    if request != None and name != '':
        url= request.get_full_path()
        if re.match(r'^'+name, url):
            return 'header_navbar_active'
    return ''