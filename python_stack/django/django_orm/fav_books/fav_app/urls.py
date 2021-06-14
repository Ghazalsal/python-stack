from django.urls import path     
from . import views
urlpatterns = [
    path('', views.index),
    path('register',views.registration),
    path('login',views.login),
    path('books',views.welcome),
    path('logout',views.logout),
    path('add_book',views.add_book),
    path('books/<int:id>',views.view_book),
    path('update/<int:id>',views.update),
    path('remove/<int:id>',views.remove),
    path('addfav/<int:id>',views.addfav),

    path('delete/<int:id>',views.delete),

]