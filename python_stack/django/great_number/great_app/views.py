from django.shortcuts import redirect, render
import random

def index(request):
    request.session['random']= random.randint(1, 100)
    return render(request,'index.html')

def rand(request):
    
    if int(request.POST['random1']) > request.session['random']:
        return render(request,'index1.html')
    if int(request.POST['random1']) < request.session['random']:
        return render(request,'index2.html')
    if int(request.POST['random1']) == request.session['random']:
        return render(request,'index3.html')
    
