from django.urls import path
from . import views

urlpatterns = [
    path('', views.massages_home, name='massages_home'),  
    path('reserve/<int:massage_id>/', views.reserve_massage, name='reserve_massage'),
    path('create/', views.create_massage, name='create_massage'),
    path('update/<int:massage_id>/', views.update_massage, name='update_massage'),
    path('delete/<int:massage_id>/', views.delete_massage, name='delete_massage'),
    path('register/', views.register, name='register'),
]