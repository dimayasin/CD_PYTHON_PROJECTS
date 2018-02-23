from __future__ import unicode_literals
from django.shortcuts import render,redirect
from django.contrib import messages
from .models import Courses

# Create your views here.

def index(request):
    courses = Courses.objects.all()
    # request.session.clear()    
    context ={
        'courses': courses
    }
    return render(request,"course/index.html", context)

def add(request):

    errors = Courses.objects.validateCourseData(request.POST)

    if len(errors)>0:
        
        for error in errors:
            messages.error(request,error)
        return redirect("/")

    else:
        Courses.objects.create(name=request.POST['cname'],description=request.POST['description'])
        return redirect("/show")

def show(request):
    context = {
        'course':Courses.objects.all()
    }

    return redirect("/",context)


def delete(request, id):
    Courses.objects.filter(id=id).delete()
    return redirect("/show")

