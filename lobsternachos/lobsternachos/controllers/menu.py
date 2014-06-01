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
  if request.method == 'GET':

    # Get categories and add to template
    categoriesList = Category.query(ancestor=GetAncestor()).fetch()
    template_values = {
        'categoriesList': categoriesList,
    }

    # If category id is long, add to template
    if isLong(request.GET.get('categoryID') ):
      template_values.update({'categoryID': long(request.GET.get('categoryID'))})

    # For every category load a list of items
    itemLists = []
    for category in categoriesList:
      subList = Item.query(Item.CategoryID == category.key,
        ancestor=GetAncestor()).fetch()
      # Append to itemLists
      itemLists.append(subList)

    # If the number of categories is different than 0, add to template
    if len(itemLists) <> 0:
      template_values.update({'itemLists': itemLists})
    return render(request, 'lobsternachos/menu/index.html',template_values)
  return render(request, 'lobsternachos/menu/index.html')

def new(request):
  if request.method == "GET":

    # Create upload url and add to template
    uploadUrl = blobstore.create_upload_url('/blobstore/upload')
    template_values = {
        'uploadUrl': uploadUrl,
    }

    # Check if category id is valid, send to template too
    if isLong(request.GET.get('categoryID') ):
      template_values.update({'categoryID': long(request.GET.get('categoryID'))})

    return render(request, 'lobsternachos/menu/new.html', template_values)
  return HttpResponseRedirect('/menu')

def create(request):
  if request.method == 'POST':
    # Create empty category
    item = Item(parent=GetAncestor())

    # If there exist the needed parameters
    if isLong(request.POST.get('categoryID')) \
    and request.POST.get('itemName') and request.POST.get('description') \
    and isLong(request.POST.get('calories')) and request.POST.get('price') and \
    request.POST.get('image1') and request.POST.get('image2'):
      # Fill item data
      item.ItemName = request.POST.get('itemName')
      item.Calories = long(request.POST.get('calories'))
      item.Description = request.POST.get('description')

      #Thumbnail = ndb.BlobKeyProperty()

      item.CategoryID = ndb.Key(Category, long(request.POST.get('categoryID')),
      parent=GetAncestor())

      item.Price = float(request.POST.get('price'))
      item.Likes = 0

      if(request.POST.get('active') == "on"):
        item.Active = True
      else:
        item.Active = False

      if(request.POST.get('dailySpecial') == "on"):
        item.DailySpecial = True
      else:
        item.DailySpecial = False

      item.ImagePath = [BlobKey(request.POST.get('image1')) ,BlobKey(request.POST.get('image2'))]

      item.put().integer_id()

      # Redirect with category id
      return HttpResponseRedirect('/menu?' +  urllib.urlencode({'categoryID':request.POST.get('categoryID')}))
  return HttpResponseRedirect('/menu')

def edit(request):
    return render(request, 'lobsternachos/menu/edit.html')

def delete(request):

  if request.method == 'POST':
    if isLong(request.POST.get('categoryID')):
      itemsList = request.POST.getlist('item')
      for itemID in itemsList:
        # Check if table id is long
        if isLong( itemID):
          # Try to get item
          item = Item.get_by_id(long(itemID),
          parent = GetAncestor())
          # Check if exist
          if item:
            item.key.delete()
      return HttpResponseRedirect('/menu?' +  urllib.urlencode({'categoryID':request.POST.get('categoryID')}))
  return HttpResponseRedirect('/menu')


  
