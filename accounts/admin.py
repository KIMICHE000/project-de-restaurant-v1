from django.contrib import admin
from .models import Client, Restaurateur, Commande, Plat, Avis, Paiement, Panier, LigneDeCommande

# Inline pour afficher les plats directement sous chaque restaurateur
class PlatInline(admin.TabularInline):
    model = Plat
    extra = 1

# Inline pour les lignes de commande
class LigneDeCommandeInline(admin.TabularInline):
    model = LigneDeCommande
    extra = 1

# Inline pour les paiements
class PaiementInline(admin.TabularInline):
    model = Paiement
    extra = 1

@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ('prenom', 'nom', 'email')
    search_fields = ('prenom', 'nom', 'email')

@admin.register(Restaurateur)
class RestaurateurAdmin(admin.ModelAdmin):
    list_display = ('prenom', 'nom', 'email')
    search_fields = ('prenom', 'nom', 'email')
    # Ajoute les plats du restaurateur dans sa fiche admin
    inlines = [PlatInline]
    
@admin.register(Plat)
class PlatAdmin(admin.ModelAdmin):
    list_display = ('nom', 'restaurateur', 'prix', 'quantite_en_stock')
    search_fields = ('nom',)
    list_filter = ('quantite_en_stock', 'restaurateur')
    
@admin.register(Commande)
class CommandeAdmin(admin.ModelAdmin):
    list_display = ('id', 'client', 'restaurateur', 'date_commande', 'statut')
    list_filter = ('statut', 'date_commande')
    search_fields = ('client__nom', 'restaurateur__nom')
    inlines = [LigneDeCommandeInline, PaiementInline]

@admin.register(Avis)
class AvisAdmin(admin.ModelAdmin):
    list_display = ('client', 'restaurateur', 'note', 'date_avis')
    list_filter = ('note', 'date_avis')
    search_fields = ('client__nom', 'restaurateur__nom')

@admin.register(Paiement)
class PaiementAdmin(admin.ModelAdmin):
    list_display = ('commande', 'montant', 'date_paiement')
    list_filter = ('date_paiement',)
    search_fields = ('commande__id',)

@admin.register(Panier)
class PanierAdmin(admin.ModelAdmin):
    list_display = ('client', 'date_creation')
    search_fields = ('client__nom',)
    list_filter = ('date_creation',)

@admin.register(LigneDeCommande)
class LigneDeCommandeAdmin(admin.ModelAdmin):
    list_display = ('commande', 'plat', 'quantite')
    list_filter = ('plat',)