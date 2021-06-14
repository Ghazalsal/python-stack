from django.urls import path
from . import views
urlpatterns = [
    path('', views.index),
    path('auth',views.index2),
    path('addbook',views.add_book),
    path('addauth',views.add_auth),
    path('get-info/<int:id>',views.get_info),
    path('add_authtobook/<int:id>',views.addauth_book),
    
]