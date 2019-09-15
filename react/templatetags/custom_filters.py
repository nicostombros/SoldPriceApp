from django.template import Library
register = Library()

@register.filter(name='ranged') 
def ranged(number):
    return range(number)
