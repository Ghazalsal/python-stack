from django.urls import path     
from . import views
urlpatterns = [
    path('', views.index),
    path('register',views.registration),
    path('login',views.login),
    path('thoughts',views.welcome),
    path('logout',views.logout),
    path('addthought',views.addthought),
    path('thoughts/<int:id>',views.details),
    path('like/<int:id>',views.like),
    path('unlike/<int:id>',views.unlike),
    path('delete/<int:id>',views.delete),
    path('dashboard',views.dashboard),
]