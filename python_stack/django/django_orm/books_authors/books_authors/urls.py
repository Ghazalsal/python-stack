from django.urls import path, include
urlpatterns = [
    path('', include('books_auth_app.urls')),
    
]