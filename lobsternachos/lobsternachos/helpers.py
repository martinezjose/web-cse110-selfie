import json
import datetime
from django.shortcuts import render
from django.http import HttpResponseRedirect
import sys
from google.appengine.api import users
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required

from lobsternachos.models import *

from lobsternachos.helpers import *
import urllib

import os

from google.appengine.ext import ndb

# Checks if value is long
def isLong(value):
  if value is not None:
    try:
      long(value)
      return True
    except ValueError:
      return False
  return False

def getTax(value):
  return 0.0825*value

# Converts native python objects to their string json representation
class Encoder(json.JSONEncoder):

  def default(self, obj):
    if isinstance(obj, datetime.datetime):
      #yyyy-MM-dd HH:mm:ss
      return obj.strftime('%Y-%m-%d %H:%M:%S')

    return json.JSONEncoder.default(self, obj)

def checkLogin(request):
  if users.get_current_user():
    if  users.get_current_user().email() <> "martinez.jose.armando@gmail.com":
      return HttpResponseRedirect(users.create_login_url(request.get_full_path()))
  else:
    return HttpResponseRedirect(users.create_login_url(request.get_full_path()))
