from lobsternachos.models import *
import json
from google.appengine.ext import ndb
from lobsternachos.helpers import Encoder
from django.http import HttpResponse
from lobsternachos.helpers import *
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse


@csrf_exempt
def post_by_table_id(request):
  if request.method == 'POST':
    if isLong( request.POST.get('tableID') ):

        # Try to get table
        table = Table.get_by_id(long(request.POST.get('tableID')),
        parent = GetAncestor())

        if(table):

          pings = Ping.query(Ping.TableID == table.key, Ping.StatusID == 0, ancestor=GetAncestor()).fetch()

          for ping in pings:
            ping.key.delete()


          pings = Ping.query(Ping.TableID == table.key, Ping.StatusID == 1,ancestor=GetAncestor()).fetch()

          for ping in pings:
            ping.key.delete()

          # Create ping
          ping = Ping( parent = GetAncestor())
          ping.TableID = table.key
          ping.StatusID = 0

          pingKey = ping.put()

          data = json.dumps({
            'PingID':pingKey.integer_id(),
            'TableID':ping.TableID.integer_id(),
            'Created':ping.Created,
            'LastUpdated':ping.LastUpdated,
            'StatusID':ping.StatusID
            }
            , cls = Encoder)

          return HttpResponse(data, content_type="application/json")

    return HttpResponse(json.dumps([]), content_type="application/json")


# Get all pings from database, and return the list as a json string
def get_all(request):
  if request.method == 'GET':
      pings = Ping.query(ancestor=GetAncestor()).fetch()

      data = json.dumps([{
        'PingID':p.key.integer_id(),
        'TableID':p.TableID.integer_id(),
        'Created':p.Created,
        'LastUpdated':p.LastUpdated,
        'StatusID':p.StatusID
      }
        for p in pings]    , cls = Encoder)

      return HttpResponse(data, content_type="application/json")

  return HttpResponse(json.dumps([]), content_type="application/json")
