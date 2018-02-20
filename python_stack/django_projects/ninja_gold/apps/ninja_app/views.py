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

  if not 'counter' in request.session:
    request.session['counter'] = 0

 
  return render(request,'survey/index.html')
