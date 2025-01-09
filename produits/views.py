from django.shortcuts import render, get_object_or_404
from .models import Produit

def produits_home(request):
    
    query = request.GET.get('q')  
    categorie = request.GET.get('categorie')  

    if query and categorie:
        
        produits = Produit.objects.filter(name__icontains=query, categorie=categorie)
    elif query:
    
        produits = Produit.objects.filter(name__icontains=query)
    elif categorie:
        
        produits = Produit.objects.filter(categorie=categorie)
    else:
       
        produits = Produit.objects.all()

    return render(request, 'produits/produits_home.html', {
        'produits': produits,
        'query': query,
        'categorie': categorie,
    })


def produit_detail(request, produit_id):
   
    produit = get_object_or_404(Produit, id=produit_id)
    return render(request, 'produits/detail.html', {'produit': produit})
