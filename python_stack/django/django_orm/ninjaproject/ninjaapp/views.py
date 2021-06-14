from django.http.response import FileResponse
from django.shortcuts import redirect, render	
from . models import dojos, ninjas

def index(request):

    context = {
        'dojo' : dojos.objects.all(),
        'ninja' : ninjas.objects.all(),
        
    }
    return render(request, "index.html", context)

def index1(request):
    dojos.objects.create(name = request.POST['name'], city = request.POST['city'], state = request.POST['state'])
    return redirect('/')

def index2(request):
    ninjas.objects.create(first_name = request.POST['first_name'], last_name = request.POST['last_name'], dojo = dojos.objects.get(name=request.POST['dojo']))
    return redirect('/')

def index3(request,id):

    dict={
            "dojo":dojos.objects.get(id=id),
            "ninja":ninjas.objects.get(id=id),
    }
    return render(request,"index.html",id)