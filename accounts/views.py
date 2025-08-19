# accounts/views.py

from django.shortcuts import render

def home(request):
    return render(request, 'accounts/home.html')

def menu(request):
    return render(request, 'accounts/menu.html')

def contact(request):
    return render(request, 'accounts/contact.html')

def commander(request):
    return render(request, 'accounts/commander.html')

def panier(request):
    return render(request, 'accounts/panier.html')

def reservation(request):
    return render(request, 'accounts/reservation.html')
