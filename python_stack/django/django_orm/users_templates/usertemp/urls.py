from django.urls import path     
from . import views
urlpatterns = [
    path('', views.index),
    path('result', views.newuser),
    path('get/<int:id>',views.getuser)
]