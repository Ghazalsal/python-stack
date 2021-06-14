from django.urls import path     
from . import views
urlpatterns = [
    path('', views.index),
    path('addbook',views.book),
    path('book/<int:idf>',views.addbook),
    path('adda',views.adda),
    path('book/labook/<int:id>',views.labook),
    path('auth', views.index1),
    path('addauth',views.auth),
    path('auth/<int:id>',views.addauth),
    path('last/<int:id>',views.last),
]