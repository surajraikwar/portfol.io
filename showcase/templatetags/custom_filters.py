from django import template

register = template.Library()

@register.filter(name='split')
def split(value, key):
    """
    Returns the value turned into a list.
    """
    return value.split(key)

@register.filter(name='trim')
def trim(value):
    """
    Strips leading and trailing whitespace.
    """
    return value.strip()
