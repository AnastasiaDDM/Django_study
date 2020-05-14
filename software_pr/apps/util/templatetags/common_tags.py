from django import template
from django.template import loader, Node, Variable
from django.utils.encoding import smart_str
from django.template.defaulttags import url
from django.template import VariableDoesNotExist

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
        if int(first_num) > int(second_num):
            return True

    return False


@register.filter(name='reverse_for_star')
def reverse_for_star(num):
    if str(num).isdigit():

        return 6 - int(num)

    return 0

    

    
                    #     {% for num_star in rating %}

                    #     {% if num_star|comparison_numbers:form.star.value %} 
                    #    d- {{num_star}}
                    #    ss- {{num_star|reverse_for_star}}


                    #     <input type="radio" id="star-{{num_star|reverse_for_star}}" name="star" value="{{num_star|reverse_for_star}}">
                    #     <label for="star-{{num_star|reverse_for_star}}" title="Оценка «{{num_star|reverse_for_star}}»"></label>	

                    #     {% else %}
                    #     буу- {{num_star}}
                    #     ss- {{num_star|reverse_for_star}}

                    #     <input type="radio" checked id="star-{{num_star|reverse_for_star}}" name="star" value="{{num_star|reverse_for_star}}">
                    #     <label for="star-{{num_star|reverse_for_star}}" title="Оценка «{{num_star|reverse_for_star}}»"></label>	

                    #     {% endif %}
                    #     {% endfor %}










                        #                     {% for num_star in rating %}

                        # {% if num_star|reverse_for_star|comparison_numbers:form.star.value %} 
                        # <input type="radio" checked id="star-{{num_star|reverse_for_star}}" name="star" value="{{num_star|reverse_for_star}}">
                        # <label for="star-{{num_star|reverse_for_star}}" title="Оценка «{{num_star|reverse_for_star}}»"></label>	                        
                        # {% else %}
                        # <input type="radio" id="star-{{num_star|reverse_for_star}}" name="star" value="{{num_star|reverse_for_star}}">
                        # <label for="star-{{num_star|reverse_for_star}}" title="Оценка «{{num_star|reverse_for_star}}»"></label>	
                        # {% endif %}
                        # {% endfor %}