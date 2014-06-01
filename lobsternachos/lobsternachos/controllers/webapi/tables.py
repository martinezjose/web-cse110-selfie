from lobsternachos.models import *
import json
from google.appengine.ext import ndb
from lobsternachos.helpers import Encoder
from django.http import HttpResponse

def get_all(request):

  data = json.dumps([{
    'TableID':p.key.integer_id(),
    'TableName':p.TableName,
    'Created':p.Created,
    'LastUpdated':p.LastUpdated}
    for p in Table.query(ancestor=GetAncestor()).fetch()], cls = Encoder)

  return HttpResponse(data, content_type="application/json")
