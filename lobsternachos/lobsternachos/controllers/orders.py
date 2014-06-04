from django.shortcuts import render
from lobsternachos.models import *
from google.appengine.ext import ndb
from lobsternachos.helpers import *
from google.appengine.ext import blobstore
from django.http import HttpResponseRedirect
from django.http import HttpResponse
import urllib
from google.appengine.ext.blobstore import BlobKey
from lobsternachos.helpers import *

def index(request):
    return render(request, 'lobsternachos/orders/index.html')

def details(request):
  if  users.get_current_user():
    if  users.get_current_user().email() <> "martinez.jose.armando@gmail.com":
      return HttpResponseRedirect(users.create_login_url(request.get_full_path()))
  else:
    return HttpResponseRedirect(users.create_login_url(request.get_full_path()))



  if request.method == 'GET':
    if isLong(request.GET.get('orderID')) :
      order = Order.get_by_id(long(request.GET.get('orderID')),parent = GetAncestor())
      if order:
        # Get pings and add to template
        table = Table.get_by_id(long(order.TableID.integer_id()),parent = GetAncestor())
        if table:

          detailsList = []

          detailsL = OrderDetail.query(OrderDetail.OrderID == order.key,ancestor=GetAncestor()).fetch()
          sumSub = 0.0
          totalSum = 0.0
          for orderItem in detailsL:
            item = Item.get_by_id(orderItem.ItemID.integer_id(),parent = GetAncestor())
            sumSub += item.Price * orderItem.Quantity
            sb = item.Price * orderItem.Quantity
            detailsList.append({ 'item':item, "orderDetail":orderItem,"subtotal": sb})

          tax = getTax(sumSub)
          total = tax+sumSub

          pingsList = Ping.query(ancestor=GetAncestor()).order(Ping.Created).fetch()
          ordersG = Order.query(Order.StatusID == 0,ancestor=GetAncestor()).order(Order.Created).fetch()


          template_values = {
              'orderDetails':detailsList,
              'tax':tax,
              'subtotal':sumSub,
              'total':total,
              'order':order,
              "tableName":table.TableName,
              'pingsList':pingsList,
              'ordersG':ordersG
          }

          return render(request, 'lobsternachos/orders/invoice.html',template_values)


  return render(request, 'lobsternachos/orders/invoice.html')

def edit(request):
    return render(request, 'lobsternachos/orders/edit.html')

def destroy(request):
    return render(request, 'lobsternachos/orders/destroy.html')
