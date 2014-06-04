from django.http import HttpResponseRedirect
from lobsternachos.models import *
from google.appengine.ext import ndb
import urllib
from lobsternachos.helpers import *

def create(request):

  if  users.get_current_user():
    if  users.get_current_user().email() <> "martinez.jose.armando@gmail.com":
      return HttpResponseRedirect(users.create_login_url(request.get_full_path()))
  else:
    return HttpResponseRedirect(users.create_login_url(request.get_full_path()))


  if request.method == 'POST':
    # Create empty category
    category = Category(parent=GetAncestor())

    # If there exist a name parameter
    if request.POST.get('categoryName'):
      # Assign and include
      category.CategoryName=request.POST.get('categoryName')
      categoryID = category.put().integer_id()

      # Redirect with category id
      return HttpResponseRedirect('/menu?' +  urllib.urlencode({'categoryID':categoryID}))
  return HttpResponseRedirect('/menu')

def delete(request):

  if  users.get_current_user():
    if  users.get_current_user().email() <> "martinez.jose.armando@gmail.com":
      return HttpResponseRedirect(users.create_login_url(request.get_full_path()))
  else:
    return HttpResponseRedirect(users.create_login_url(request.get_full_path()))


  if request.method == 'POST':
    # Check if category id is long
    if isLong( request.POST.get('categoryID') ):
      # Try to get category
      category = Category.get_by_id(long(request.POST.get('categoryID')),
      parent = GetAncestor())
      # Check if exist
      if category:
        category.key.delete()
  return HttpResponseRedirect('/menu')

def update(request):
  if  users.get_current_user():
    if  users.get_current_user().email() <> "martinez.jose.armando@gmail.com":
      return HttpResponseRedirect(users.create_login_url(request.get_full_path()))
  else:
    return HttpResponseRedirect(users.create_login_url(request.get_full_path()))


  if request.method == 'POST':
    # Check if category id is long
    if isLong( request.POST.get('categoryID') ):
      # Try to get category
      category = Category.get_by_id(long(request.POST.get('categoryID')),
      parent = GetAncestor())
      # If exist and category name is present
      if category and request.POST.get('categoryName'):
        # Update
        category.CategoryName = request.POST.get('categoryName')
        categoryID = category.put().integer_id()

        #Redirect with category id
        return HttpResponseRedirect('/menu?' +  urllib.urlencode({'categoryID':categoryID}))
  return HttpResponseRedirect('/menu')
