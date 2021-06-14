from django.urls import path, include
urlpatterns = [
    path('', include('great_app.urls')),
]