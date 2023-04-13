from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect,get_object_or_404
from django.urls import reverse

from selfapp.forms import CourseForm
from selfapp.models import Department,Courses


# Create your views here.
def home(request):

    return render(request,'home.html',)

def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        cpassword = request.POST['password1']
        if password == cpassword:
            if User.objects.filter(username=username).exists():

                return redirect('register')
            else:
                user = User.objects.create_user(username=username, password=password,)
                user.save();
                return redirect('/login')
        else:
            messages.info(request, "password not matching")
            return redirect('register')

    return render(request,'register.html')

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('/enroll')
        else:
            messages.info(request, "invalid credentials")
            return redirect('/login')

    return render(request,'login.html')

def enroll(request):

    return render(request,'enroll.html')

def info(request):
    dept=Department.objects.all()
    course=Courses.objects.all()
    form = CourseForm(request.POST or None,request.FILES)
    if form.is_valid():
        form.save()
        messages.info(request,"order confirmed")
        return redirect('/confirm')

    return render(request,'demo.html',{'dept':dept,'course':course,'form':form})

def confirm(request):
     messages.add_message(request, messages.INFO, 'Hello world.')
     return render(request,'work.html')