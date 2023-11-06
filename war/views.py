from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Q

from django.contrib.auth.decorators import login_required

from .models import *

@login_required(login_url='account_signup')
def home(request):
    cartas = Carta.objects.all() 
    search = request.GET.get('search') if request.GET.get('search') != None else ""
    cartas = Carta.objects.filter(
        Q(nome__icontains = search) |
        Q(ataque__icontains = search) |
        Q(vida__icontains = search) |
        Q(data_lancamento__icontains = search) |
        Q(tipo__nome__icontains = search) 
    )
    
    print(cartas.count())    
    
    context = {'cartas' : cartas}
    return render(request, 'html/base.html', context)

def habilidades(request, id):
    carta = get_object_or_404(Carta, id = id)
    habilidades = Habilidade.objects.filter(carta=carta)
    
    print(f' Carta : {carta}')
    print(habilidades[0])       
    
    context={'carta' : carta, 'habilidades': habilidades,}
    return render(request, 'habilidades.html', context)

def campeoes(request):
    return
def fight(request, pk):
    carta = get_object_or_404(Carta, id = pk)
    bot = Carta.objects.order_by('?').first
    context = {'carta' : carta, 'bot' : bot}
    return render(request, 'fight.html', context)