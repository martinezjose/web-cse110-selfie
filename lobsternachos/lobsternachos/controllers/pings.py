from django.http import HttpResponseRedirect
from lobsternachos.models import *
from google.appengine.ext import ndb
import urllib
from lobsternachos.helpers import *
from django.http import HttpResponse


def delete(request):

  if  users.get_current_user():
    if  users.get_current_user().email() <> "martinez.jose.armando@gmail.com":
      return HttpResponseRedirect(users.create_login_url(request.get_full_path()))
  else:
    return HttpResponseRedirect(users.create_login_url(request.get_full_path()))


  # Check if category id is long
  if isLong( request.GET.get('pingID') ):
    # Try to get category
    ping = Ping.get_by_id(long(request.GET.get('pingID')),
    parent = GetAncestor())
    # Check if exist
    if ping:
      ping.key.delete()
  return HttpResponseRedirect('/')

def update(request):
  if  users.get_current_user():
    if  users.get_current_user().email() <> "martinez.jose.armando@gmail.com":
      return HttpResponseRedirect(users.create_login_url(request.get_full_path()))
  else:
    return HttpResponseRedirect(users.create_login_url(request.get_full_path()))



  if request.method == 'POST':
    # Check if category id is long
    if isLong( request.POST.get('pingID') ) and isLong( request.POST.get('statusID') ):


      ping = Ping.get_by_id(long(request.POST.get('pingID')),parent=GetAncestor())

      if ping:
        ping.StatusID = long(request.POST.get('statusID'))


      pingKey = ping.put()

      return HttpResponse(pingKey)
  return HttpResponse('')
