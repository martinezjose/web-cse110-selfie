from django.shortcuts import render
from lobsternachos.models import *
from google.appengine.ext import ndb
from lobsternachos.helpers import *
from google.appengine.ext import blobstore
from django.http import HttpResponseRedirect
from django.http import HttpResponse
import urllib
from google.appengine.ext.blobstore import BlobKey
from google.appengine.api import users
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required


def index(request):

    if  users.get_current_user():
      if  users.get_current_user().email() <> "martinez.jose.armando@gmail.com":
        return HttpResponseRedirect(users.create_login_url(request.get_full_path()))
    else:
      return HttpResponseRedirect(users.create_login_url(request.get_full_path()))


    if request.method == 'GET':


      pingsList = Ping.query(ancestor=GetAncestor()).order(Ping.Created).fetch()
      ordersG = Order.query(Order.StatusID == 0,ancestor=GetAncestor()).order(Order.Created).fetch()


      # Get categories and add to template
      categoriesList = Category.query(ancestor=GetAncestor()).fetch()
      template_values = {
          'categoriesList': categoriesList,
          'pingsList':pingsList,
          'ordersG':ordersG
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

    if  users.get_current_user():
      if  users.get_current_user().email() <> "martinez.jose.armando@gmail.com":
        return HttpResponseRedirect(users.create_login_url(request.get_full_path()))
    else:
      return HttpResponseRedirect(users.create_login_url(request.get_full_path()))


    if request.method == "GET":


      # Get categories and add to template
      categoriesList = Category.query(ancestor=GetAncestor()).fetch()


      categoriesWithItems = 0

      # For every category load a list of items
      itemLists = []
      for category in categoriesList:
        subList = Item.query(Item.CategoryID == category.key,
          ancestor=GetAncestor()).fetch()
        itemLists.append(subList)

        if len(subList) <> 0:
          # Append to itemLists
          categoriesWithItems = categoriesWithItems + 1

      template_values = {
          'categoriesList': categoriesList
      }

      # Check if category id is valid, send to template too
      if isLong(request.GET.get('categoryID') ):
        template_values.update({'categoryID': long(request.GET.get('categoryID'))})
        for category in categoriesList:
          if category.key.integer_id() == long(request.GET.get('categoryID')):
            template_values.update({'categoryName':category.CategoryName})


      # If the number of categories is different than 0, add to template
      if categoriesWithItems > 0:
        template_values.update({'itemLists': itemLists})

      return render(request, 'lobsternachos/menu/new.html', template_values)
    return HttpResponseRedirect('/menu')

def create(request):
    if  users.get_current_user():
      if  users.get_current_user().email() <> "martinez.jose.armando@gmail.com":
        return HttpResponseRedirect(users.create_login_url(request.get_full_path()))
    else:
      return HttpResponseRedirect(users.create_login_url(request.get_full_path()))


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


        itemKey = item.put()

        if request.POST.getlist('recommendedItemIDs'):
          recItemIDs = request.POST.getlist('recommendedItemIDs')
          for recItemID in recItemIDs:

            # Check if rec item id is long
            if isLong(recItemID):

              # Try to get item
              item = Item.get_by_id(long(recItemID),
              parent = GetAncestor())

              if(item):

                recommendation = Recommendation(
                parent = GetAncestor())

                recommendation.RecommendedItemID = item.key
                recommendation.ItemID = itemKey
                recommendation.put()
              # Check if exist
              #if table:
              #  table.key.delete()

        # Redirect with category id
        return HttpResponseRedirect('/menu?' +  urllib.urlencode({'categoryID':request.POST.get('categoryID')}))
    return HttpResponseRedirect('/menu')


def update(request):
    if  users.get_current_user():
      if  users.get_current_user().email() <> "martinez.jose.armando@gmail.com":
        return HttpResponseRedirect(users.create_login_url(request.get_full_path()))
    else:
      return HttpResponseRedirect(users.create_login_url(request.get_full_path()))


    if request.method == 'POST':


      # If there exist the needed parameters
      if isLong(request.POST.get('itemID')) and isLong(request.POST.get('categoryID')) \
      and request.POST.get('itemName') and request.POST.get('description') \
      and isLong(request.POST.get('calories')) and request.POST.get('price') and \
      request.POST.get('image1') and request.POST.get('image2'):

        # Try to get item
        item = Item.get_by_id(long(request.POST.get('itemID')),
          parent = GetAncestor())

        if(item):

          # Fill item data
          item.ItemName = request.POST.get('itemName')
          item.Calories = long(request.POST.get('calories'))
          item.Description = request.POST.get('description')

          item.CategoryID = ndb.Key(Category, long(request.POST.get('categoryID')),
          parent=GetAncestor())

          item.Price = float(request.POST.get('price'))

          if(request.POST.get('active') == "on"):
            item.Active = True
          else:
            item.Active = False

          if(request.POST.get('dailySpecial') == "on"):
            item.DailySpecial = True
          else:
            item.DailySpecial = False

          item.ImagePath = [BlobKey(request.POST.get('image1')) ,BlobKey(request.POST.get('image2'))]

          itemKey = item.put()

          recommendedItems = Recommendation.query(Recommendation.ItemID == itemKey,
            ancestor=GetAncestor()).fetch()

          for recommendedItem in recommendedItems:
              recommendedItem.key.delete()


          if request.POST.getlist('recommendedItemIDs'):

            recItemIDs = request.POST.getlist('recommendedItemIDs')

            for recItemID in recItemIDs:

              # Check if rec item id is long
              if isLong(recItemID):

                # Try to get item
                itemR = Item.get_by_id(long(recItemID),
                parent = GetAncestor())

                if(itemR):

                  recommendation = Recommendation(
                  parent = GetAncestor())

                  recommendation.RecommendedItemID = itemR.key
                  recommendation.ItemID = itemKey
                  recommendation.put()

            recommendedItems = Recommendation.query(Recommendation.ItemID == itemKey,
              ancestor=GetAncestor()).fetch()

          # Redirect with category id
          return HttpResponseRedirect('/menu?' +  urllib.urlencode({'categoryID':request.POST.get('categoryID')}))
    return HttpResponseRedirect('/menu')

def edit(request):

    if  users.get_current_user():
      if  users.get_current_user().email() <> "martinez.jose.armando@gmail.com":
        return HttpResponseRedirect(users.create_login_url(request.get_full_path()))
    else:
      return HttpResponseRedirect(users.create_login_url(request.get_full_path()))


    if request.method == "GET":

      # Check if itemID and categoryID exist
      if isLong(request.GET.get('itemID') ) and isLong(request.GET.get('categoryID') ):

        # Try to get item
        item = Item.get_by_id(long(request.GET.get('itemID')),
        parent = GetAncestor())

        if(item):
          # Get categories and add to template
          categoriesList = Category.query(ancestor=GetAncestor()).fetch()

          # Add category and categories list to template values
          template_values = {
            'categoriesList': categoriesList,
            'categoryID': long(request.GET.get('categoryID')),
            'itemObj' : item
          }

          # Initialize counter
          categoriesWithItems = 0

          # For every category load a list of items and append to itemLists
          itemLists = []
          for category in categoriesList:
            subList = Item.query(Item.CategoryID == category.key,
              ancestor=GetAncestor()).fetch()
            itemLists.append(subList)

            # Find the category from the item, add it to template
            if category.key.integer_id() == long(request.GET.get('categoryID')):
                template_values.update({'categoryName':category.CategoryName})

            # If an item was found in the sub list, increment counter
            if len(subList) <> 0:
              # Append to itemLists
              categoriesWithItems = categoriesWithItems + 1


          # If the number of categories is different than 0, add to template
          if categoriesWithItems > 0:
            template_values.update({'itemLists': itemLists})

          #Recommendation(ndb.Model):
          #ItemID =  ndb.KeyProperty(kind=Item,required=True)
          #RecommendedItemID =  ndb.KeyProperty(kind=Item,required=True

          recommendedItems = Recommendation.query(Recommendation.ItemID == item.key,
            ancestor=GetAncestor()).fetch()

          template_values.update({'recommendedItems': recommendedItems})



          return render(request, 'lobsternachos/menu/edit.html', template_values)
    return HttpResponseRedirect('/menu')

def delete(request):
  if  users.get_current_user():
    if  users.get_current_user().email() <> "martinez.jose.armando@gmail.com":
      return HttpResponseRedirect(users.create_login_url(request.get_full_path()))
  else:
    return HttpResponseRedirect(users.create_login_url(request.get_full_path()))


  if users.get_current_user():

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
