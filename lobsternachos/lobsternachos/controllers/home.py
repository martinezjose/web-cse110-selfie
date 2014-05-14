from django.shortcuts import render
from django.http import HttpResponseRedirect

from google.appengine.api import users

from lobsternachos.models import *

import urllib

import os

from google.appengine.ext import ndb

DEFAULT_GUESTBOOK_NAME = 'default_guestbook'


# We set a parent key on the 'Greetings' to ensure that they are all in the same
# entity group. Queries across the single entity group will be consistent.
# However, the write rate should be limited to ~1/second.

def guestbook_key(guestbook_name=DEFAULT_GUESTBOOK_NAME):
    """Constructs a Datastore key for a Guestbook entity with guestbook_name."""
    return ndb.Key('Guestbook', guestbook_name)

class Greeting(ndb.Model):
    """Models an individual Guestbook entry with author, content, and date."""
    author = ndb.UserProperty()
    content = ndb.StringProperty(indexed=False)
    date = ndb.DateTimeProperty(auto_now_add=True)

def main_page(request):
    guestbook_name = request.GET.get('guestbook_name', DEFAULT_GUESTBOOK_NAME)

    greetings_query = Greeting.query(
            ancestor=guestbook_key(guestbook_name)).order(-Greeting.date)
    greetings = greetings_query.fetch(10)

    if users.get_current_user():
        url = users.create_logout_url(request.get_full_path())
        url_linktext = 'Logout'
    else:
        url = users.create_login_url(request.get_full_path())
        url_linktext = 'Login'

    template_values = {
        'greetings': greetings,
        'guestbook_name': urllib.quote_plus(guestbook_name),
        'url': url,
        'url_linktext': url_linktext,
    }
    return render(request, 'lobsternachos/main_page.html', template_values)

def sign_post(request):

# We set the same parent key on the 'Greeting' to ensure each Greeting
# is in the same entity group. Queries across the single entity group
# will be consistent. However, the write rate to a single entity group
# should be limited to ~1/second.

  if request.method == 'POST':
    guestbook_name = request.GET.get('guestbook_name', DEFAULT_GUESTBOOK_NAME)

    greeting = Greeting(parent=guestbook_key(guestbook_name))

    if users.get_current_user():
      greeting.author = users.get_current_user()

    greeting.content = request.POST.get('content')
    greeting.put()

    return HttpResponseRedirect('/?' + urllib.urlencode({'guestbook_name': guestbook_name}))
  return HttpResponseRedirect('/')
