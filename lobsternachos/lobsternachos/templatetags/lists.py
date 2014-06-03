from django import template

register = template.Library()

@register.filter
def get_at_position(list, index):
    return list[index-1]

@register.filter
def isRecommended(item, recommended):
  found = False

  for recItem in recommended:
    if recItem.RecommendedItemID == item.key:
      found = True
      break

  return found
