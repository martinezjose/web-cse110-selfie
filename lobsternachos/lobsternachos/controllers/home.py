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


#def main_page(request):
    #guestbook_name = request.GET.get('guestbook_name', DEFAULT_GUESTBOOK_NAME)
    #cat = Category()
    #greetings_query = Greeting.query(
    #        ancestor=guestbook_key(guestbook_name)
    #        ).order(-Greeting.date)
    #greetings = greetings_query.fetch(100)

    #if users.get_current_user():
    #    url = users.create_logout_url(request.get_full_path())
    #    url_linktext = 'Logout'
    #else:
    #    url = users.create_login_url(request.get_full_path())
    #    url_linktext = 'Login'

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



#@login_required(login_url='/accounts/login')
def index(request):

    if  users.get_current_user():
      if  users.get_current_user().email() <> "martinez.jose.armando@gmail.com":
        return HttpResponseRedirect(users.create_login_url(request.get_full_path()))
    else:
      return HttpResponseRedirect(users.create_login_url(request.get_full_path()))


    if request.method == 'GET':

      # Get pings and add to template
      pingsList = Ping.query(ancestor=GetAncestor()).order(Ping.Created).fetch()
      tablesList = Table.query(ancestor=GetAncestor()).fetch()
      ordersList = Order.query(Order.StatusID == 0,ancestor=GetAncestor()).order(Order.Created).fetch()
      fatOrdersList = []
      for order in ordersList:

        details = OrderDetail.query(OrderDetail.OrderID == order.key,ancestor=GetAncestor()).fetch()
        sumSub = 0.0
        for orderItem in details:
          item = Item.get_by_id(orderItem.ItemID.integer_id(),parent = GetAncestor())
          sumSub += item.Price * orderItem.Quantity

        tax = getTax(sumSub)
        total = tax+sumSub
        fatOrdersList.append({ 'order':order, "items":len(details),"total":total })


      template_values = {
          'pingsList': pingsList,
          'tablesList': tablesList,
          'fatOrdersList': fatOrdersList,
          'logoutURL':users.create_logout_url(request.get_full_path())
      }

      return render(request, 'lobsternachos/home/index.html',template_values)
    return render(request, 'lobsternachos/home/index.html')




def contact(request):
  return render(request, 'lobsternachos/home/contact.html')

def faq(request):
    return render(request, 'lobsternachos/home/faq.html')


# Accounts
def profile(request):
    return render(request, 'lobsternachos/accounts/profile.html')
def login(request):
    return render(request, 'lobsternachos/accounts/login.html')
def lock_screen(request):
    return render(request, 'lobsternachos/accounts/lock_screen.html')
