from django.urls import path, include
urlpatterns = [
    path('', include('dojo_app.urls')),
]