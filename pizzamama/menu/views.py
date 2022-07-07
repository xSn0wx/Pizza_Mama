from django.shortcuts import render
from django.http import HttpResponse
from django.core import serializers
from .models import Pizza
# Create your views here.

def index(request):
    '''pizzas = Pizza.objects.all()
    pizza_names_and_price = [pizza.nom + " : " + str(pizza.prix) + "€" for pizza in pizzas]
    pizza_names_and_prices_str = ", ".join(pizza_names_and_price)
    return HttpResponse("Les pizzas : " + pizza_names_and_prices_str)'''
    pizzas = Pizza.objects.all().order_by('prix')
    return render(request, 'menu/index.html', {'pizzas' : pizzas})

def api_get_pizzas(requests):
    pizzas = Pizza.objects.all().order_by('prix')
    json = serializers.serialize("json", pizzas)
    return HttpResponse(json)