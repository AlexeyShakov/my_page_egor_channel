# This file serves us for creating own HTML filters

from django import template
from django.template.defaultfilters import stringfilter

# We will be registering new filters by using this variable. We'll be using it as decorator
register = template.Library()

# Value will be splitted by key
@register.filter(name="split")
# The decorator below guarantees that the input of function(value) is a string
@stringfilter
def split(value, key=" "):
    return value.split(key)
