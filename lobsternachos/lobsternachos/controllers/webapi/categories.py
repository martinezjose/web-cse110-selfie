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

          #strftime('We are the %d, %b %Y')
#'We are the 22, Nov 2008'
#All the letter after a "%" represent a format for something :

#%d is the day number
#%m is the month number
#%b is the month abbreviation
#%y is the year last two digits
#%Y is the all year
#yyyy-MM-dd HH:mm:ss
            return obj.strftime('%Y-%m-%d %H:%M:%s')

        return json.JSONEncoder.default(self, obj)


def get_all(request):

  #data = json.dumps()

  data = json.dumps([p.to_dict() for p in Category.query(ancestor=GlobalAncestor()).fetch()], cls = MyEncoder)


  return HttpResponse(data, content_type="application/json")
      # Get all items from database, and return the list as a json string
