from django.urls import path     
from . import views
urlpatterns = [
    path('', views.index),
    path('register',views.registration),
    path('login',views.login),
    path('success',views.welcome),
    path('logout',views.logout),
    path('post_msg',views.post_msg),
    path('post_comm/<int:id>',views.post_comm),
]