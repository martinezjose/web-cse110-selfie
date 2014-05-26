from django.shortcuts import render
from django.http import HttpResponseRedirect
import sys
from google.appengine.api import users

from lobsternachos.models import *
from django.core import serializers
import json

import urllib

import os

from google.appengine.ext import ndb


import json
import datetime
from time import mktime

from django.http import HttpResponse

class MyEncoder(json.JSONEncoder):

  def default(self, obj):
    if isinstance(obj, datetime.datetime):
      #yyyy-MM-dd HH:mm:ss
      return obj.strftime('%Y-%m-%d %H:%M:%S')

    return json.JSONEncoder.default(self, obj)

def get_all(request):

	data = json.dumps([{
	'ItemID':p.ItemID,
	'RecommendedItemID':p.RecommendedItemID,
  'Created':p.Created,
  'LastUpdated':p.LastUpdated} 
   for p in Recommendation.query(ancestor=GlobalAncestor()).fetch()], cls = MyEncoder)
	
	return HttpResponse(data, content_type="application/json")
  