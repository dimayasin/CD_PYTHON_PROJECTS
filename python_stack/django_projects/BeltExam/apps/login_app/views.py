# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render,redirect,HttpResponse
from django.contrib import messages
import bcrypt
from .models import Users
from .models import Posts

secret_key = 'TARDIS' 


def index(request):
    users = Users.objects.all()
    # request.session['name'] = ""

    context ={
        'users': users
    }
    return render(request,"index.html", context)

def log(request):
    return render(request,"login.html")

def logins(request):
    errors = Users.objects.validateLoginData(request.POST)
    if len(errors)>0:
        for error in errors:
            messages.error(request,error)
        return redirect("/login")
    else:
        users = Users.objects.filter(email = request.POST['email'])
        context={
            'users': users
        }
        return redirect("/show"+id)

def Registration(request):
    errors = Users.objects.validateRegistrationData(request.POST)
    if len(errors)>0:
        for error in errors:
            messages.error(request,error)
        return render(request,"/new_user")
    else:
        hasher1 = bcrypt.hashpw(request.POST['psswrd'].encode(), bcrypt.gensalt())
        Users.objects.create( name=request.POST['name'],email=request.POST['email'], password=hasher1, DOB= request.POST['dob'])
        users = Users.objects.filter(email = request.POST['email'])
        context={
            'users': users
        }
        # request.session['id'] = users[0].id
        # request.session['name'] = users[0].name 

        return render(request,"appt_form.html", context)

def new_user(request):
    return render(request,"registration.html")

def Newappointments(request):
    user = Users.objects.filter(id=id)
    this_user = user[0]
    errors = Posts.objects.ValidatePosts(request.POST)
    if len (errors)>0:
        for error in errors:
            messages.error(request,error)
        return render(request,"/show"+id)
    else:

        Posts.objects.create( name=request.POST['task'],time=request.POST['time'], status="Pending", date= request.POST['date'], user= request.session['id'])
        posting = Posts.objects.filter(user = id )
        context={
            'posts': posting
        }
        return redirect("/show"+id)

def update(request,id):
    posts = Posts.objects.filter(id=id)
    edit_post = posts[0]
    if request.POST['task']:
        edit_post.task = request.POST['task']
        edit_post.save()
    if request.POST['status']:
        edit_post.status = request.POST['status']
        edit_post.save()
    if request.POST['date']:
        edit_post.date = request.POST['date']
        edit_post.save()
    if request.POST['time']:
        edit_post.time = request.POST['time']
        edit_post.save()

    return redirect("/show"+id)

def delete(request, id):
    Users.objects.filter(id=id).delete()
    return redirect("/show"+id)

def out(request,id):
    request.session.clear()
    return redirect ("/login")

def show(request,id):
    context={
        "posts": Posts.objects.all(user = id)}
    return render(request, "appointment.html", context)
