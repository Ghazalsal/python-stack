from django.shortcuts import redirect, render, HttpResponse
from . import models
from .models import Books,Authors
def index(request):
    context = {
        'books' : models.Books.objects.all(),
    }
    return render(request,'index.html',context)

def book(request):
    Books.objects.create(title=request.POST['title'],desc= request.POST['desc'])
    return redirect ('/')

def addbook(request,idf):
    
    context = {
        'books' : Books.objects.all(),
        'author': Authors.objects.get(id=idf),
        'id':Books.objects.get(id=idf),
        'authors': Authors.objects.all()
    }
    return render(request,'addbook.html',context)


def adda(request):
    id=Books.objects.get(id=id)
    context = {
        'books' : Books.objects.all(),
        'authors': Authors.objects.all(),
        'id': id
    }
    return redirect('book/<int:id>')


def labook(request,id):
    
    ver= Authors.objects.get(id=request.POST['sel'])
    x= Books.objects.get(id=id)
    x.Author.add(ver)
    context = {
        'books' : Books.objects.all(),
        'author': Authors.objects.get(id=id),
        'id':Books.objects.get(id=id),
        'authors': Authors.objects.all()
    }
    return render(request,'addbook.html',context)


def index1(request):
    context = {
        'authors' : models.Authors.objects.all(),
    }
    return render(request,'index1.html',context)

def auth(request):
    Authors.objects.create(first_name=request.POST['first_name'],last_name= request.POST['last_name'],book= Authors.objects.get(name=request.POST['book']),notes=request.POST['notes'])
    return redirect ('auth')

def addauth(request,id):

    context = {
        'author' : Authors.objects.get(id=id),
        'books' : Books.objects.all(),

    }
    return render(request,'addauth.html',context)

def last(request,id):
    
    ver= Authors.objects.get(id=id)
    x= Books.objects.get(id=request.POST['sel'])
    ver.book.add(x)
    context = {
        'author' : Authors.objects.get(id=id),
        'books' : Books.objects.all(),

    }
    return render(request,'addauth.html',context)


