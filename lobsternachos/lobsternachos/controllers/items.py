from django.shortcuts import render
from django.http import HttpResponseRedirect
from google.appengine.api import users
from lobsternachos.models import *
import urllib
import os
from google.appengine.ext import ndb


def index(request):
    category_list = Category.query().fetch()
    template_values = {
        'category_list': category_list,
    }
    return render(request, 'lobsternachos/items/index.html',template_values)

def show(request):
    return render(request, 'lobsternachos/items/show.html')

def new(request):
    return render(request, 'lobsternachos/items/new.html')

def edit(request):
    return render(request, 'lobsternachos/items/edit.html')

def destroy(request):
    return render(request, 'lobsternachos/items/destroy.html')
