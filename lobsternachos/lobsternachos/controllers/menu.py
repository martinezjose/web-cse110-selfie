from django.shortcuts import render
from lobsternachos.models import *
from google.appengine.ext import ndb
from django.http import HttpResponse

def index(request):
    categoryID=request.GET.get('categoryID')
    categoriesList = Category.query(ancestor=GetAncestor()).fetch()
    template_values = {
        'categoriesList': categoriesList,
    }

    if categoryID is not None:
      template_values.update({'categoryID':int(categoryID)})

    return render(request, 'lobsternachos/menu/index.html',template_values)

def show(request):
    return render(request, 'lobsternachos/menu/show.html')

def new(request):

    return render(request, 'lobsternachos/menu/new.html')

def edit(request):
    return render(request, 'lobsternachos/menu/edit.html')

def destroy(request):
    return render(request, 'lobsternachos/menu/destroy.html')
