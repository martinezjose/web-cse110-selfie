from lobsternachos.models import *
import json
from google.appengine.ext import ndb
from lobsternachos.helpers import Encoder
from django.http import HttpResponse
from lobsternachos.helpers import *

# Get tables from database that have a defined pairing code, and return the list as a json string
def get_by_pairing_code(request):
  if request.method == 'GET':

    if isLong( request.GET.get('pairingCode') ):

        # Try to get category
        tableList = Table.query( Table.PairingCode==long(request.GET.get('pairingCode')),ancestor = GetAncestor()).fetch()
        # If exist and category name is present
        if len(tableList) == 1:

          # Get table
          table = tableList[0]


          data = json.dumps({
            'TableID':table.key.integer_id(),
            'TableName':table.TableName,
            'Created':table.Created,
            'LastUpdated':table.LastUpdated,
            'PairingCode':table.PairingCode
            }
            , cls = Encoder)

          return HttpResponse(data, content_type="application/json")
    else:
      # Try to get category
      tableList = Table.query(ancestor = GetAncestor()).fetch()


      data = json.dumps([{
        'TableID':p.key.integer_id(),
        'TableName':p.TableName,
        'Created':p.Created,
        'LastUpdated':p.LastUpdated,
        'PairingCode':p.PairingCode
        } for p in tableList]
        , cls = Encoder)

      return HttpResponse(data, content_type="application/json")

    return HttpResponse(json.dumps([]), content_type="application/json")
