from django.db import models


class Book(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Author(models.Model):
    first_name = models.CharField(max_length=255, default="author")
    last_name = models.CharField(max_length=255, default="default")
    notes = models.TextField()
    books = models.ManyToManyField(Book, related_name="Authors")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

def getBook():
    return Book.objects.all().values()


  

def addBook(form):
    return Book.objects.create(title = form["title"] , description =  form['description'])

def bookID(id):
    book = Book.objects.get(id = id)
    return book

def getAuthors():
    return Book.objects.all().values()

def Addauthor():
    return Author.objects.all().values()
def idauthor(id):
    return Author.objects.get(id = id)

def authorBook(id,form):
    author = Author.objects.get(id =int(form["select"]))
   
    book = Book.objects.get(id = id)
    x = book.Authors.add(author)
    return x

def getAuthor():
    books = Author.objects.all().values()
    return books

def addAuthor(form):
    return Author.objects.create(title = form["title"] , description =  form['description'])

def authorID(id):
    book = Author.objects.get(id = id)
    return book

def bookAuthor(id,form):
    book = Book.objects.get(id =int(form["select"]))
   
    author = Author.objects.get(id = id)
    x = book.Authors.add(author)
    return x
    
