from lobsternachos.models import *
import json
from google.appengine.ext import ndb
from lobsternachos.helpers import Encoder
from django.http import HttpResponse
import datetime

# Get all items from database, and return the list as a json string
def get_all(request):
  if request.method == 'GET':

    categoriesList = Category.query(ancestor=GetAncestor()).fetch()
    validCategories = []

    for category in categoriesList:
      if len(Item.query(Item.CategoryID == category.key,Item.Active == True,ancestor=GetAncestor()).fetch()) >0:
        validCategories.append(category)


    data = json.dumps([{
      'CategoryID':p.key.integer_id(),
      'CategoryName':p.CategoryName,
      'Created':p.Created,
      'LastUpdated':p.LastUpdated } for p in validCategories], cls = Encoder)

    return HttpResponse(data, content_type="application/json")
