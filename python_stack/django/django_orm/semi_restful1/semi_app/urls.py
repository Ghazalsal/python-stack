from django.urls import path     
from . import views
urlpatterns = [
    path('', views.index),
    path('shows',views.show),
    path('shows/new',views.new),
    path('shows/new/render',views.newrender),
    path('shows/<int:data>',views.view),
    path('shows/<int:data>/edit',views.edit),
    path('shows/render/edit',views.editrender),
    path('shows/<int:data>/delete',views.delete)
]