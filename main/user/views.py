from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from . models import product

# Create your views here.
def loginpage(request):
    if 'username' in request.session:
        return redirect('items')
    if request.method == "POST":
        username=request.POST['username']
        password=request.POST['password']
        
        user=authenticate(username=username,password=password)
        if user is not None:
            request.session['username']=username
            return redirect('items')
            # login(request,user)
            
            # return render(request,'items.html')
        else:
            return redirect("login")
        
    return render(request,'login.html')

def signup(request):
    if request.method == "POST":
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        
        
        myuser=User.objects.create_user(username,email,password)
        myuser.save()
        
        return redirect('login')
    
    return render(request,'signup.html')
def home(request):
    return render(request,'home.html')

def items(request):
    if 'username' in request.session:
        products = product.objects.all()
        
        return render(request,'items.html',{'products':products})
    return redirect('login')

def user_logout(request):
    if 'username' in request.session:
        request.session.flush()
    return redirect('login')
