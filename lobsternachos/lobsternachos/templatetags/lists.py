from django import template

register = template.Library()

@register.filter
def get_at_position(list, index):
    return list[index-1]
