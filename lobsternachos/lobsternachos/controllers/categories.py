from django.http import HttpResponseRedirect
from lobsternachos.models import *
from google.appengine.ext import ndb
import urllib

def create(request):
  if request.method == 'POST':
    category = Category(parent=GetAncestor())
    if request.POST.get('categoryName'):
      category.CategoryName=request.POST.get('categoryName')
      categoryID = category.put().integer_id()
      return HttpResponseRedirect('/menu?' +  urllib.urlencode({'categoryID':categoryID}))
  return HttpResponseRedirect('/menu')

def delete(request):
  if request.method == 'POST':
    category = Category.get_by_id(int(request.POST.get('categoryID')),
    parent = GetAncestor())
    category.key.delete()
  return HttpResponseRedirect('/menu')

def update(request):
  if request.method == 'POST':
    category = Category.get_by_id(int(request.POST.get('categoryID')),
    parent = GetAncestor())
    if category and request.POST.get('categoryName'):
      category.CategoryName = request.POST.get('categoryName')
      categoryID = category.put().integer_id()
      return HttpResponseRedirect('/menu?' +  urllib.urlencode({'categoryID':categoryID}))
  return HttpResponseRedirect('/menu')
