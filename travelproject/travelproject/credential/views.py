from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.shortcuts import render, redirect

# Create your views here.

def login(request):
    if request.method=='POST':
        username=request.POST['Username']
        password=request.POST['Password']
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.info(request,"invalid credential")
            return redirect('login')
    return render(request,"login.html")
def register(request):
    if request.method== 'POST':
        username=request.POST['Username']
        firstname=request.POST['First_name']
        lastname=request.POST['Last_name']
        email=request.POST['email']
        password=request.POST['password']
        confirmpassword=request.POST['cpassword']
        if password ==confirmpassword:
            if User.objects.filter(username=username).exists():
                messages.info(request,"username taken")
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request,"email already taken")
                return redirect('register')
            user=User.objects.create_user(username=username,first_name=firstname,last_name=lastname,email=email,password=password)
            user.save()
            print("user created")
            return redirect('login')
        else:
            messages.info(request,"password doesn't match")
    return render(request,"register.html")
def logout(request):
    auth.logout(request)
    return redirect('/')

