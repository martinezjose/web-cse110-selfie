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

def new(request):

    uploadUrl = blobstore.create_upload_url('/blobstore/upload')
    template_values = {
        'uploadUrl': uploadUrl,
    }
    if isLong(request.GET.get('categoryID') ):
      template_values.update({'categoryID': long(request.GET.get('categoryID'))})

    return render(request, 'lobsternachos/menu/new.html', template_values)

def uploadImage(request):
    print(request)
    return HttpResponse(request)

def create(request):
  if request.method == 'POST':
    # Create empty category
    item = Item(parent=GetAncestor())

    # If there exist a name parameter
    if isLong(request.POST.get('categoryID')) \
    and request.POST.get('itemName') and request.POST.get('description') \
    and isLong(request.POST.get('calories')) and request.POST.get('price') and \
    request.POST.get('image1') and request.POST.get('image2') :
      item.ItemName = request.POST.get('itemName')
      item.Calories = long(request.POST.get('calories'))
      item.Description = request.POST.get('description')

      #ImagePath = ndb.BlobKeyProperty(repeated=True)
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

      itemID = item.put().integer_id()

      # Redirect with category id
      return HttpResponseRedirect('/menu?' +  urllib.urlencode({'categoryID':request.POST.get('categoryID')}))
  return HttpResponseRedirect('/menu')

def edit(request):
    return render(request, 'lobsternachos/menu/edit.html')

def destroy(request):
    return render(request, 'lobsternachos/menu/destroy.html')
