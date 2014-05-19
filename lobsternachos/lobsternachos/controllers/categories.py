from django.shortcuts import render
from django.http import HttpResponseRedirect
import sys
from google.appengine.api import users

from lobsternachos.models import *


import urllib

import os

from google.appengine.ext import ndb

def new(request):

  if request.method == 'POST':

    category = Category()
    category.CategoryName=request.POST.get('CategoryName')
    if category.CategoryName:
      category.put()

    return HttpResponseRedirect('/items?')
  return HttpResponseRedirect('/items')
