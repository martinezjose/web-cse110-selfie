from django.shortcuts import render
from django.http import HttpResponseRedirect
from google.appengine.api import users
from lobsternachos.models import *
import urllib
from google.appengine.ext import ndb
from Django_AppEngine.userbackend import *

def login(request):
    backend = CustomRemoteUserBackend()
    backend.get_user('Admin')
    if backend.authenticate():
      return render(request, 'lobsternachos/accounts/login?yes')
