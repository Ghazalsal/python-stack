from django.shortcuts import redirect, render, HttpResponse
from login_app.models import User
from django.contrib import messages
import bcrypt
def index(request):
    if 'user' in request.session:
        return redirect('/success')
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
            password = request.POST['password']
            pw_hash = bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()
            User.objects.create(first_name=first_name,last_name=last_name,email=email, password=pw_hash)
        
        
            messages.success(request, "Registration/Login successfully updated")
            return redirect('/success')
    return redirect('/success')

def login(request):
    errors = User.objects.valid(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/')
    else:
        
        
        user = User.objects.filter(email=request.POST['email']) # why are we using filter here instead of get?
        
        
        if user:
            logged_user = user[0]
            if bcrypt.checkpw(request.POST['password'].encode(), user.password.encode()):
            # if we get True after checking the password, we may put the user id in session
                request.session['userid'] = user.id
            # never render on a post, always redirect!
                return redirect('/success')
        
        messages.success(request, "Registration/Login successfully updated")
    print(request.POST['email'])
    email= request.POST['email']
    password = request.POST['password']
    if email == "" or password =="":
        return redirect('/')
    users = User.objects.filter(email=email)
    if len(users)== 0:
        return redirect('/')
    user=users.first()
    if user.password != password:
        return redirect('/')
    data={
        'first_name':user.first_name, 
        'email':user.email,
        'password' :user.password,
        
    }
    request.session['user']=data
    
    return redirect('/success')
    

def welcome(request):

    if 'user' in request.session:
        first_name= request.session['user']['first_name']
        contet={
            'first_name':first_name
        }
        return render(request,'welcome.html',contet)
    return redirect('/')

def logout(request):
    if 'user' in request.session:
        request.session.clear()
    return redirect('/')


