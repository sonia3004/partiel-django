from django.db import models

class Produit(models.Model):
    CATEGORIES = [
        ('soin', 'Soin'),
        ('beauté', 'Beauté'),
        ('relaxation', 'Relaxation'),
    ]

    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='produits_images/')
    categorie = models.CharField(max_length=50, choices=CATEGORIES, default='soin')

    def __str__(self):
        return self.name
