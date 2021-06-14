from django.shortcuts import redirect, render
from . import models
from .models import Books,Authors
def index(request):
    context={
        'all_books': Books.objects.all()
    }
    return render(request,'index.html',context)
def index2(request):
    context={
        'all_auth': Authors.objects.all()
    }
    return render(request,'index2.html',context)

def add_book(request):
    Books.objects.create(title=request.POST['title'],desc=request.POST['desc'])
    return redirect('/')

def add_auth(request):
    Authors.objects.create(first_name=request.POST['first_name'],last_name=request.POST['last_name'],notes=request.POST['notes'])
    return redirect('/auth')

def get_info(request,id):
    book=Books.objects.get(id=id)
    context={
        'book': book,
        'all_auth': Authors.objects.all(),
        'writers': book.authors.all()
    }
    return render(request,'get-info.html',context)

def addauth_book(request,id):
    this_book = Books.objects.get(id=id)
    this_auth= Authors.objects.get(id =request.POST['author'])
    this_auth.books.add(this_book)
    return redirect('/get-info/{}'.format(id))