# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse, redirect

# Create your views here.


def index(request):
    if not 'gold' in request.session:
        request.session['gold'] = 0
        request.session['msg'] = ""

    return render(request, 'ninja/index.html')


def process(request):
    timer = request.session['counter']
    timer += 1
    request.session['counter'] = timer
    context = {
        'name': request.POST['name'],
        'location': request.POST['location'],
        'language': request.POST['language'],
        'comment': request.POST['comment'],
        'counter': request.session['counter']
    }

    return render(request, "survey/results.html", context)
