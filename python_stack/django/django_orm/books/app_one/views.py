from django.shortcuts import redirect, render
from . import models
def books(request):

    context = {
        "books" : models.getBook()
    }

    return render(request, "books.html", context)

def addBook(request):
    models.addBook(request.POST)
    return redirect('/')

def bookDetails(request, id):

    context = {
        "books": models.bookID(id),
        "authors": models.Addauthor(),
        
        

    }
    return render(request, "bookDetails.html", context)
    


def addaAuthors(request, id):

    models.authorBook(id, request.POST)
    
    return redirect("/books/" +str(id))

#################################3
def authors(request):

    context = {
        "authors" : models.getAuthor()
    }

    return render(request, "authors.html", context)

def addAuthor(request):
    models.addAuthor(request.POST)
    return redirect('/authors')

def authorDetails(request, id):

    context = {
        "book": models.getBook(),
        "authors": models.authorID(id),
        
        
    }
    return render(request, "authorDetails.html", context)
    
###################################
def addBooks(request, id):

    models.bookAuthor(id, request.POST)
    
    return redirect("/authors/" +str(id))





