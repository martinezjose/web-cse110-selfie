from django.shortcuts import render
from django.http import HttpResponseRedirect
from google.appengine.api import users
from lobsternachos.models import *
import urllib
from google.appengine.ext import ndb
from Django_AppEngine.userbackend import *

def login(request):
    #if request.method == 'POST':
      #backend = CustomRemoteUserBackend()

      #request.META['REMOTE_USER'] = backend.authenticate()
      #if request.META['REMOTE_USER']:
      #  return HttpResponseRedirect('/asd/')
      #else:
      #template_values = {
      #    'error': 'The email or password you entered is incorrect.',
      #    'user':request.META['REMOTE_USER']
      #}
      return render(request, 'lobsternachos/accounts/login.html')#,template_values)
    #return render(request, 'lobsternachos/accounts/login.html')

      #template_values = {
      #    'greetings': greetings,
      #     'guestbook_name': urllib.quote_plus(guestbook_name),
      #    'url': url,
      #    'url_linktext': url_linktext,
      #
      #}
      #return render(request, 'lobsternachos/main_page.html', template_values)

  #def sign_post(request):

  # We set the same parent key on the 'Greeting' to ensure each Greeting
  # is in the same entity group. Queries across the single entity group
  # will be consistent. However, the write rate to a single entity group
  # should be limited to ~1/second.

    #if request.method == 'POST':
    #  guestbook_name = request.GET.get('guestbook_name', DEFAULT_GUESTBOOK_NAME)

    #  greeting = Greeting(parent=guestbook_key(guestbook_name))

    #  if users.get_current_user():
    #    greeting.author = users.get_current_user()


    #  greeting.content = request.POST.get('content')
    #  greeting.put()

    #  return HttpResponseRedirect('/?' + urllib.urlencode({'guestbook_name': guestbook_name}))
    #return HttpResponseRedirect('/')
