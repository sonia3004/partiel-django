from django.urls import path
from . import views

urlpatterns = [
    path('', views.produits_home, name='produits_home'),
    path('<int:produit_id>/', views.produit_detail, name='produit_detail'),
]
