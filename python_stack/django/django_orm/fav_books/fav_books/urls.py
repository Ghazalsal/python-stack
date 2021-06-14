from django.urls import path, include
urlpatterns = [
    path('', include('fav_app.urls')),
]