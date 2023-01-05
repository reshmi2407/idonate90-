from email import message
from django.shortcuts import render,redirect
from django.contrib import messages
from .models import Signup

# Create your views here.

def home(request):
    return render(request, "index.html")

def signup(request):
    if request.method=="POST":
        username=request.POST['username']
        email=request.POST['email']
        password=request.POST['password']

        global val
        def val():
            return username

        if Signup.objects.filter(username=username,email=email):
            messages.error(request,"User already exist")
            return render(request,"login.html")

        #messages.success(request,"Your account has created successfully")
        myprofile=Signup(username=username,email=email,password=password)
        myprofile.save()
        messages.success(request,"Your account has created successfully")
        
        return render(request,"news.html")
    
    return render(request,"login.html")

def login(request):
    if request.method =='POST':
        username=request.POST['username']
        password=request.POST['password']

        credential=Signup.objects.all()
        flag=0
        for i in credential:
            if i.username==username and i.password==password:
                flag=1
                global val
                def val():
                    return username
                return render(request,"news.html")
        if flag==0:
            messages.error(request,"Bad Credentials")
            return redirect('home')

    return render(request,"login.html")

def signout(request):
    messages.success(request,"Logged Out successfully!")
    return redirect('home')

