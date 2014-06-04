from django.shortcuts import render
from lobsternachos.models import *
from google.appengine.ext import ndb
from lobsternachos.helpers import *
from google.appengine.ext import blobstore
from django.http import HttpResponseRedirect
from django.http import HttpResponse
import urllib
from google.appengine.ext.blobstore import BlobKey


def index(request):

  if  users.get_current_user():
    if  users.get_current_user().email() <> "martinez.jose.armando@gmail.com":
      return HttpResponseRedirect(users.create_login_url(request.get_full_path()))
  else:
    return HttpResponseRedirect(users.create_login_url(request.get_full_path()))


  if request.method == 'GET':



    pingsList = Ping.query(ancestor=GetAncestor()).order(Ping.Created).fetch()
    ordersG = Order.query(Order.StatusID == 0,ancestor=GetAncestor()).order(Order.Created).fetch()


    # Get tables and add to template
    tablesList = Table.query(ancestor=GetAncestor()).fetch()
    template_values = {
        'tablesList': tablesList,
        'pingsList':pingsList,
        'ordersG':ordersG
    }

    return render(request, 'lobsternachos/tables/index.html',template_values)
  return render(request, 'lobsternachos/tables/index.html')

def create(request):

  if  users.get_current_user():
    if  users.get_current_user().email() <> "martinez.jose.armando@gmail.com":
      return HttpResponseRedirect(users.create_login_url(request.get_full_path()))
  else:
    return HttpResponseRedirect(users.create_login_url(request.get_full_path()))


  if request.method == 'POST':
    # Create empty table
    table = Table(parent=GetAncestor())

    # If there exist a name parameter
    if request.POST.get('tableName'):
      # Assign and include
      table.TableName=request.POST.get('tableName')

      # Generate initial pairing code
      pairingCode = randint(1000,9999)

      # While it already exists within a table, generate another one
      while len(Table.query( Table.PairingCode==pairingCode,ancestor = GetAncestor()).fetch()) <> 0:
        pairingCode = randint(1000,9999)

      table.PairingCode = pairingCode

      tableID = table.put().integer_id()

  return HttpResponseRedirect('/tables')

def delete(request):

  if  users.get_current_user():
    if  users.get_current_user().email() <> "martinez.jose.armando@gmail.com":
      return HttpResponseRedirect(users.create_login_url(request.get_full_path()))
  else:
    return HttpResponseRedirect(users.create_login_url(request.get_full_path()))


  if request.method == 'POST':
    tablesList = request.POST.getlist('table')
    for tableID in tablesList:
      # Check if table id is long
      if isLong( tableID):
        # Try to get table
        table = Table.get_by_id(long(tableID),
        parent = GetAncestor())
        # Check if exist
        if table:
          table.key.delete()
  return HttpResponseRedirect('/tables')

def update(request):

  if  users.get_current_user():
    if  users.get_current_user().email() <> "martinez.jose.armando@gmail.com":
      return HttpResponseRedirect(users.create_login_url(request.get_full_path()))
  else:
    return HttpResponseRedirect(users.create_login_url(request.get_full_path()))


  if request.method == 'POST':
    # Check if table id is long
    if isLong( request.POST.get('tableID') ):
      # Try to get table
      table = Table.get_by_id(long(request.POST.get('tableID')),
      parent = GetAncestor())
      # If exist and table name is present
      if table and request.POST.get('tableName'):
        # Update
        table.TableName = request.POST.get('tableName')
        tableID = table.put().integer_id()

  return HttpResponseRedirect('/tables')
