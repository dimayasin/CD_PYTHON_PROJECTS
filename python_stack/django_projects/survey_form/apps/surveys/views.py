# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse, redirect

# Create your views here.
def index(request):
  # if not 'number' in session:
  #       session['name'] = ""
  #       session['location'] = ""
  #       session['language'] = ""
  #       session['comment'] = ""
 
  return render(request,'survey/index.html')

def process(request):
  context = {
  "name": request.form['name'],
  "location":request.form['location'],
  "language":request.form['language'],
  "comment":request.form['comment']
    }

  return render(request,"survey/results.html", context)