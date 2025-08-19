# accounts/models.py

from django.db import models
from django.utils import timezone

class Client(models.Model):
    """Représente un client de l'application."""
    nom = models.CharField(max_length=100)
    prenom = models.CharField(max_length=100)
    email = models.EmailField(unique=True)

    def __str__(self):
        return f"{self.prenom} {self.nom}"
    
class Restaurateur(models.Model):
    """Représente un restaurateur ou une entité de restaurant."""
    nom = models.CharField(max_length=100)
    prenom = models.CharField(max_length=100)
    email = models.EmailField(unique=True)

    def __str__(self):
        return f"{self.prenom} {self.nom}"

class Plat(models.Model):
    """Représente un plat proposé par un restaurateur."""
    # Le plat est lié au restaurateur qui le vend.
    restaurateur = models.ForeignKey(Restaurateur, on_delete=models.CASCADE, null=True)
    nom = models.CharField(max_length=100)
    prix = models.DecimalField(max_digits=6, decimal_places=2)
    quantite_en_stock = models.IntegerField(default=0)
    
    def __str__(self):
        return f"{self.nom} - {self.prix}€"

class Commande(models.Model):
    """Représente une commande passée par un client."""
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    restaurateur = models.ForeignKey(Restaurateur, on_delete=models.CASCADE)
    date_commande = models.DateTimeField(default=timezone.now)
    statut = models.CharField(max_length=20, choices=[('en cours', 'En cours'), ('livrée', 'Livrée')], default='en cours')
    
    def __str__(self):
        return f"Commande {self.id} - {self.client.prenom} {self.client.nom} - {self.statut}"

class LigneDeCommande(models.Model):
    """Représente un article (plat) à l'intérieur d'une commande."""
    commande = models.ForeignKey(Commande, on_delete=models.CASCADE)
    plat = models.ForeignKey(Plat, on_delete=models.CASCADE)
    quantite = models.IntegerField(default=1)
    prix = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return f"{self.quantite} x {self.plat.nom} dans la commande {self.commande.id}"

class Avis(models.Model):
    """Représente un avis et une note d'un client."""
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    restaurateur = models.ForeignKey(Restaurateur, on_delete=models.CASCADE)
    note = models.IntegerField()
    commentaire = models.TextField(blank=True, null=True)
    date_avis = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"Avis de {self.client.prenom} {self.client.nom}"

class Paiement(models.Model):
    """Représente une transaction de paiement."""
    commande = models.ForeignKey(Commande, on_delete=models.CASCADE)
    montant = models.DecimalField(max_digits=6, decimal_places=2)
    date_paiement = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"Paiement pour Commande {self.commande.id} - {self.montant}€"
    
class Panier(models.Model):
    """Représente le panier d'un client avant la commande."""
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    date_creation = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"Panier de {self.client.prenom} {self.client.nom}"

class LigneDePanier(models.Model):
    """Représente un article (plat) à l'intérieur d'un panier."""
    panier = models.ForeignKey(Panier, on_delete=models.CASCADE)
    plat = models.ForeignKey(Plat, on_delete=models.CASCADE)
    quantite = models.IntegerField(default=1)

    def __str__(self):
        return f"{self.quantite} x {self.plat.nom} dans le panier de {self.panier.client.nom}"