from django.urls import path, include
urlpatterns = [
    path('', include('wall_app.urls')),
]