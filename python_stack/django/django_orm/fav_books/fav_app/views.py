from django.shortcuts import redirect, render, HttpResponse
from fav_app.models import User,Book
from django.contrib import messages
import bcrypt

def index(request):
    if 'user' in request.session:
        return redirect('/books')
    return render(request,'index.html')

def registration(request):
    errors = User.objects.basic_validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/')
    else:
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email=request.POST['email']
        password=request.POST['password']
        conf_password = request.POST['conf_password']
        if password == conf_password:
            pw_hash = bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()
            user= User.objects.create(first_name=first_name,last_name=last_name,email=email, password=pw_hash)
            if 'user' not in request.session:
                request.session['user']=user.id
                request.session['first_name']= first_name
                request.session['last_name']=last_name
                
            messages.success(request, "Registration/Login successfully updated")
            return redirect('/books')
        else:
            return redirect('/')

def login(request):
    if request.method=="POST":
        users = User.objects.get(email=request.POST['email'])
        errors={}
        if users:
            if 'user' not in request.session:
                request.session['user']=users.id
                request.session['first_name']= users.first_name
                request.session['password']=users.last_name
        if users:
            if bcrypt.checkpw(request.POST['password'].encode(), users.password.encode()):
                    return redirect('/books')
        errors = User.objects.basic_validator(request.POST)
        if len(errors) > 0:
            for key, value in errors.items():
                messages.error(request, value)
            return redirect('/')

def welcome(request):
    if 'user' in request.session:
        contet={
            'first_name':request.session['first_name'],
            'user':User.objects.all(),
            'book':Book.objects.all(),
        }
        return render(request,'welcome.html',contet)

def logout(request):
    if 'user' in request.session:
        request.session.clear()
    return redirect('/')

def add_book(request):
    errors = Book.objects.validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/books')
    if request.method == "POST":
        
        new_book = Book.objects.create(
            title=request.POST['title'], description=request.POST['description'], uploded_by=User.objects.get(id=request.session['user']))
        book=Book.objects.get(id= new_book.id)
        user=User.objects.get(id=request.session['user'])
        book.users_who_like.add(user)
    return redirect('/books')

def view_book(request,id):
    contet={
            'first_name':request.session['first_name'],
            'user':User.objects.all(),
            'book':Book.objects.get(id=id),
            
        }
    return render(request,'showbook.html',contet)
def update(request,id):
    if request.method == "POST":
        book=Book.objects.get(id=id)
        book.description= request.POST['description']
        book.save()
    return redirect('/books/'+str(id))

def remove(request,id):
    book=Book.objects.get(id=id)
    user=User.objects.get(id=request.session['user'])
    book.users_who_like.remove(user)
    return redirect('/books/'+str(id))

def addfav(request,id):
    book=Book.objects.get(id=id)
    user=User.objects.get(id=request.session['user'])
    book.users_who_like.add(user)
    return redirect('/books/'+str(id))

def delete(request,id):
    
    book=Book.objects.get(id=id)
    book.delete()
    return redirect('/books')