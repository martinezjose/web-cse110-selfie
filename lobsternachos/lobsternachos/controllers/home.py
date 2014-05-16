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

# Base
def blank(request):
    return render(request, 'lobsternachos/blank.html')

# UI
def widget(request):
    return render(request, 'lobsternachos/uidemos/widget.html')
def ui_element(request):
    return render(request, 'lobsternachos/uidemos/ui_element.html')
def table(request):
    return render(request, 'lobsternachos/uidemos/table.html')
def tab(request):
    return render(request, 'lobsternachos/uidemos/tab.html')
def nestable_list(request):
    return render(request, 'lobsternachos/uidemos/nestable_list.html')
def button(request):
    return render(request, 'lobsternachos/uidemos/button.html')
def form_wizard(request):
    return render(request, 'lobsternachos/uidemos/form_wizard.html')
def form_element(request):
    return render(request, 'lobsternachos/uidemos/form_element.html')


# Home
def search_result(request):
    return render(request, 'lobsternachos/home/search_result.html')
def landing(request):
  return render(request, 'lobsternachos/home/landing.html')
def index(request):
  return render(request, 'lobsternachos/home/index.html')
def contact(request):
  return render(request, 'lobsternachos/home/contact.html')
def faq(request):
    return render(request, 'lobsternachos/home/faq.html')




# Accounts
def register(request):
    return render(request, 'lobsternachos/accounts/register.html')
def profile(request):
    return render(request, 'lobsternachos/accounts/profile.html')
def login(request):
    return render(request, 'lobsternachos/accounts/login.html')
def lock_screen(request):
    return render(request, 'lobsternachos/accounts/lock_screen.html')

# Emails
def email_template_red(request):
    return render(request, 'lobsternachos/email/email_template_red.html')
def email_template_purple(request):
    return render(request, 'lobsternachos/email/email_template_purple.html')
def email_template_orange(request):
    return render(request, 'lobsternachos/email/email_template_orange.html')
def email_template_green(request):
    return render(request, 'lobsternachos/email/email_template_green.html')
def email_template_dark(request):
    return render(request, 'lobsternachos/email/email_template_dark.html')
def email_template_blue(request):
    return render(request, 'lobsternachos/email/email_template_blue.html')
def email_selection(request):
    return render(request, 'lobsternachos/email/email_selection.html')

# Temp
def blog(request):
    return render(request, 'lobsternachos/temp/blog.html')
def timeline(request):
    return render(request, 'lobsternachos/temp/timeline.html')
def single_post(request):
    return render(request, 'lobsternachos/temp/single_post.html')
def pricing(request):
    return render(request, 'lobsternachos/temp/pricing.html')
def movie(request):
    return render(request, 'lobsternachos/temp/movie.html')
def chat(request):
    return render(request, 'lobsternachos/temp/chat.html')
def calendar(request):
    return render(request, 'lobsternachos/temp/calendar.html')
def inbox(request):
    return render(request, 'lobsternachos/temp/inbox.html')
def gallery(request):
    return render(request, 'lobsternachos/temp/gallery.html')



# Orders
def invoice(request):
    return render(request, 'lobsternachos/orders/invoice.html')


# Errors
def error500(request):
    return render(request, 'customErrors/error500.html')
def error404(request):
    return render(request, 'customErrors/error404.html')
