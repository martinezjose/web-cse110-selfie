from django import template

register = template.Library()

@register.filter
def get_message(id, entity_name):
    if id is 1:
      return entity_name + ' succesfully added'
