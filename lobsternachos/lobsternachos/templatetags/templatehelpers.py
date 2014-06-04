from django import template
from datetime import datetime
import time



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

@register.filter
def getMinutesDifference(d1):
  d2 = datetime.now()

  # convert to unix timestamp
  d1_ts = time.mktime(d1.timetuple())
  d2_ts = time.mktime(d2.timetuple())

  # they are now in seconds, subtract and then divide by 60 to get minutes.
  return int(d2_ts-d1_ts) / 60
