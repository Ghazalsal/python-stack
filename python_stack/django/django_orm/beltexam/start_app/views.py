from django.shortcuts import redirect, render, HttpResponse
from start_app.models import User,Thought
from django.contrib import messages
import bcrypt

def index(request):
    if 'user' in request.session:
        return redirect('/thoughts')
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
            return redirect('/thoughts')
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
                    return redirect('/thoughts')
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
            'thought':Thought.objects.all(),
        }
        return render(request,'welcome.html',contet)

def logout(request):
    if 'user' in request.session:
        request.session.clear()
    return redirect('/')

def addthought(request):
    errors = Thought.objects.validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/thoughts')
    if request.method == "POST":
        thought = Thought.objects.create(
            thought=request.POST['thought'], uploaded_by=User.objects.get(id=request.session['user']))
        thought=Thought.objects.get(id= thought.id)
        user=User.objects.get(id=request.session['user'])
    return redirect('/thoughts')

def details(request,id):
    contet={
            'first_name':request.session['first_name'],
            'user':User.objects.all(),
            'thought':Thought.objects.get(id=id),
            
        }
    
    
    return render(request,'details.html',contet)

def like(request,id):
    thought=Thought.objects.get(id=id)
    user=User.objects.get(id=request.session['user'])
    thought.users_who_like.add(user)
    
    return redirect('/thoughts/'+str(id))

def unlike(request,id):
    thought=Thought.objects.get(id=id)
    user=User.objects.get(id=request.session['user'])
    thought.users_who_like.remove(user)
    return redirect('/thoughts/'+str(id))

def delete(request,id):
    thought=Thought.objects.get(id=id)
    thought.delete()
    return redirect('/thoughts')

def dashboard(request):
    return redirect('/thoughts')