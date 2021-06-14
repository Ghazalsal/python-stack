from django.urls import path, include
urlpatterns = [
    path('', include('counter_app.urls'))
]