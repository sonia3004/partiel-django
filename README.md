# Centre de Bien-Être - Gestion des Massages et Produits

Ce projet est une application Django qui permet de gérer un centre de bien-être. Les fonctionnalités principales incluent la gestion des massages, la consultation des produits, l'inscription des utilisateurs et la réservation de services.

## Fonctionnalités

### **1. Gestion des Massages**
- Affichage d'une liste de massages disponibles.
- Réservation de massages pour les utilisateurs inscrits.
- Gestion des massages (ajout, modification et suppression) réservée aux administrateurs.

### **2. Gestion des Produits**
- Affichage des produits de soins disponibles.
- Recherche de produits par nom.
- Filtrage des produits par catégorie (soin, beauté, relaxation).
- Consultation des détails de chaque produit.

### **3. Gestion des Utilisateurs**
- Inscription d'utilisateurs via un formulaire dédié.
- Connexion et déconnexion des utilisateurs.
- Protection des fonctionnalités (réservations, gestion des massages) par authentification.

---

## Installation et Lancement du Projet

### **1. Prérequis**
- Python 3.8 ou plus.
- Django (version utilisée dans ce projet : 5.1.4).
- Git.

### **2. Cloner le Repository**
```bash
git clone https://github.com/ton-username/ton-repository.git
cd ton-repository

3. Créer un Environnement Virtuel

python -m venv venv
source venv/bin/activate  # Sous Linux/Mac
venv\Scripts\activate     # Sous Windows

4. Installer les Dépendances

pip install -r requirements.txt

5. Configurer la Base de Données

    Appliquer les migrations :

python manage.py makemigrations
python manage.py migrate

6. Créer un Superutilisateur

python manage.py createsuperuser

7. Lancer le Serveur

python manage.py runserver

Utilisation
1. Accès à l'Application

    Page d'accueil : http://127.0.0.1:8000/

2. Massages

    Liste des massages : http://127.0.0.1:8000/massages/

3. Produits

    Liste des produits : http://127.0.0.1:8000/produits/

Structure des Dossiers

.
├── mini_massage/
│   ├── settings.py        # Configuration principale du projet Django
│   ├── urls.py            # Routes principales
│   └── wsgi.py            # Point d'entrée WSGI
├── massages/
│   ├── models.py          # Modèles pour les massages et réservations
│   ├── views.py           # Logique des vues pour les massages
│   ├── templates/
│   │   └── massages/      # Templates HTML pour les massages
│   └── forms.py           # Formulaires liés aux massages
├── produits/
│   ├── models.py          # Modèle pour les produits
│   ├── views.py           # Logique des vues pour les produits
│   ├── templates/
│   │   └── produits/      # Templates HTML pour les produits
│   └── forms.py           # Formulaires liés aux produits
├── media/                 # Dossier contenant les fichiers média (images uploadées)
├── static/                # Fichiers CSS et JavaScript
└── manage.py              # Commande d'administration Django

Fonctionnalités Techniques
1. Utilisation de Django Forms

    Formulaire pour la réservation de massages.
    Formulaire pour l'inscription d'utilisateurs.
    Validation des mots de passe dans les formulaires.

2. Sécurisation

    Utilisation des décorateurs @login_required et @user_passes_test pour protéger les routes sensibles.
    Jeton CSRF intégré pour sécuriser les formulaires.

3. Recherche et Filtrage

    Recherche de produits par mot-clé dans la barre de recherche.
    Filtrage des produits par catégorie.

4. Fichiers Média

    Gestion des images via ImageField et configuration de MEDIA_URL et MEDIA_ROOT.

Technologies Utilisées

    Langage Backend : Python
    Framework : Django
    Base de Données : SQLite (par défaut)
    Frontend : HTML, CSS (fichier style.css), et templates Django.

Améliorations Futures

    Ajouter une fonctionnalité pour afficher l'historique des réservations.
    Implémenter un système de paiement en ligne pour réserver des massages.
    Ajouter une fonctionnalité pour laisser des avis sur les produits et les massages.
    Améliorer le design de l'interface utilisateur.
