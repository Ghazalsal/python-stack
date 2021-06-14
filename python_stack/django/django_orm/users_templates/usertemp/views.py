from django.shortcuts import redirect, render,HttpResponse
from .models import users
def index(request):
    context = {
        "users": users.objects.all()
    }
    return render(request, "index.html", context)

def newuser(request):
    users.objects.create(first_name =request.POST['first_name'],last_name=request.POST['last_name'],age=request.POST['age'],email_address=request.POST['email_address'])
    
    return redirect('/')
    
def getuser(request,id):
    
    dict={
        "users":users.objects.get(id=id)
    }
    return render(request,'index1.html',dict)
