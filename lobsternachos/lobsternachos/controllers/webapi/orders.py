from lobsternachos.models import *
import json
from google.appengine.ext import ndb
from lobsternachos.helpers import Encoder
from django.http import HttpResponse

# Get all orders from database, and return the list as a json string
def get_all(request):
  if request.method == 'GET':

    data = json.dumps([{'CategoryID':p.key.integer_id(),
      'CategoryName':p.CategoryName,
      'Created':p.Created,
      'LastUpdated':p.LastUpdated} for p in Category.query(ancestor=GetAncestor()).fetch()], cls = Encoder)


    return HttpResponse(data, content_type="application/json")
