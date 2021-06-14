
from django.urls import path
from . import views



urlpatterns = [
    path('', views.books),
    path('addbook', views.addBook),
    path('books/<int:id>', views.bookDetails),
    path('addAuthors/<int:id>', views.addaAuthors),
    path('authors', views.authors),
    path('addauthor', views.addAuthor),
    path('authors/<int:id>', views.authorDetails),
    path('addBooks/<int:id>', views.addBooks),
]