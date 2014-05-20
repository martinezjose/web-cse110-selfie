from django.shortcuts import render
from django.http import HttpResponseRedirect
import sys
from google.appengine.api import users

from lobsternachos.models import *


import urllib

import os

from google.appengine.ext import ndb

def create(request):

  if request.method == 'POST':

    category = Category(parent=GlobalAncestor())
    category.CategoryName=request.POST.get('CategoryName')
    if category.CategoryName:
      catID = category.put().integer_id()
      return HttpResponseRedirect('/items?' + urllib.urlencode({'catID': catID}))
    return HttpResponseRedirect('/items')
  return HttpResponseRedirect('/items')
