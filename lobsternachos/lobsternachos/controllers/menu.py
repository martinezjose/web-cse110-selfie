from django.shortcuts import render
from django.http import HttpResponseRedirect
from google.appengine.api import users
from lobsternachos.models import *
import urllib
import os
from google.appengine.ext import ndb

from django.contrib.auth.decorators import login_required

def index(request):
    categories_list = Category.query(ancestor=GlobalAncestor()).fetch()
    template_values = {
        'categories_list': categories_list,
    }
    return render(request, 'lobsternachos/menu/index.html',template_values)

def show(request):
    return render(request, 'lobsternachos/menu/show.html')

def new(request):

    return render(request, 'lobsternachos/menu/new.html')

def edit(request):
    return render(request, 'lobsternachos/menu/edit.html')

def destroy(request):
    return render(request, 'lobsternachos/menu/destroy.html')
