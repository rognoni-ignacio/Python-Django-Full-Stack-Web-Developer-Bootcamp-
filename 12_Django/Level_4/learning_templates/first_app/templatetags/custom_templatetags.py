from django import template

register = template.Library()


@register.filter(name='custom_cut')
def custom_cut(value, arg):
    """
    This cuts out all values of "arg" from the string
    """
    return value.replace(arg, '')


# register.filter('custom_cut', custom_cut)
