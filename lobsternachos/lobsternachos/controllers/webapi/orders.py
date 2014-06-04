from lobsternachos.models import *
import json
from google.appengine.ext import ndb
from lobsternachos.helpers import Encoder
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from lobsternachos.helpers import *

@csrf_exempt
def post_by_table_id(request):
  if request.method == 'POST':

    json_data = json.loads(request.raw_post_data)

    tableID = json_data['TableID']
    orderDetails = json_data['OrderDetails']
    oneItem = False
    try:
      for detail in orderDetails:
        if not isLong(detail['ItemID']):
          return HttpResponse(detail['ItemID'])
        elif not isLong(detail['Quantity']):
          return HttpResponse(detail['Quantity'])
    except:
      oneItem = True


    # Try to get table
    table = Table.get_by_id(long(tableID),
    parent = GetAncestor())

    if table:

          order = Order(parent = GetAncestor())
          order.TableID = table.key
          order.StatusID = 0
          orderKey = order.put()

          if oneItem:
              # Get item
              item = Item.get_by_id(long(orderDetails['ItemID']),
              parent = GetAncestor())

              if item:

                orderDetail = OrderDetail(parent = GetAncestor())
                orderDetail.ItemID = item.key
                orderDetail.OrderID = orderKey
                orderDetail.Quantity = long(orderDetails['Quantity'])

                orderDetail.put()
          else:
            for detail in orderDetails:
              # Get item
              item = Item.get_by_id(long(detail['ItemID']),
              parent = GetAncestor())

              if item:

                orderDetail = OrderDetail(parent = GetAncestor())
                orderDetail.ItemID = item.key
                orderDetail.OrderID = orderKey
                orderDetail.Quantity = long(detail['Quantity'])

                orderDetail.put()


          data = json.dumps({
            'OrderID':orderKey.integer_id(),
            'TableID':order.TableID.integer_id(),
            'Created':order.Created,
            'LastUpdated':order.LastUpdated,
            'StatusID':order.StatusID
            }
            , cls = Encoder)

          return HttpResponse(data, content_type="application/json")

    return HttpResponse(json.dumps([]), content_type="application/json")
