import json
import datetime

# Checks if value is long
def isLong(value):
  if value is not None:
    try:
      long(value)
      return True
    except ValueError:
      return False
  return False

# Converts native python objects to their string json representation
class Encoder(json.JSONEncoder):

  def default(self, obj):
    if isinstance(obj, datetime.datetime):
      #yyyy-MM-dd HH:mm:ss
      return obj.strftime('%Y-%m-%d %H:%M:%S')

    return json.JSONEncoder.default(self, obj)
