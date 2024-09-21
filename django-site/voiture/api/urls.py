from django.urls import path

from . import views

urlpatterns = [
    path('garages/', views.get_garages, name='get_garages'),        
    path('garages/<int:pk>/', views.get_garage, name='get_garage'),  
    path('garages/add/', views.add_garage, name='add_garage'),       
    path('garages/<int:pk>/edit/', views.edit_garage, name='edit_garage'),  
    path('garages/<int:pk>/delete/', views.delete_garage, name='delete_garage'),  

]

