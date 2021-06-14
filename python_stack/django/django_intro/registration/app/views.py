from django.shortcuts import redirect, render,HttpResponse
from app.models import User

def index(request):
    if 'user' in request.session:
        return redirect('/welcome')
    return render(request, 'index.html')

def login(request):
    username = request.POST['username']
    password= request.POST['password']
    if username == "" or password =="":
        return redirect('/')
    users = User.objects.filter(username=username)
    if len(users)== 0:
        return redirect('/')
    user = users.first()
    if user.password != password:
        return redirect('/')
    data={
        'username':user.username,
        'email':user.email,
        'address':user.address,
        'password': user.password,
    }
    request.session['user']=data
    return redirect('/welcome')

def register(request):
    username = request.POST['username']
    email = request.POST['email']
    address = request.POST['address']
    password = request.POST['password']
    user = User.objects.create(username=username,email=email,address=address,password=password)
    data={
        'username':username,
        'email':email,
        'address':address,
        'password':password,
    }
    request.session['user']=data
    return redirect('/welcome')

def welcome(request):
    if 'user' in request.session:
        username= request.session['user']['username']
        return render(request,'welcome.html')
    return redirect('/')

def logout(request):
    if 'user' in request.session:
        request.session.clear()
    return redirect('/')