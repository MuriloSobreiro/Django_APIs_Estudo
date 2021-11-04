from django.http import response
from django.shortcuts import render

from main.forms import Pokemon
from main.pokemonGetter import getPokemon

# Create your views here.
def home(response):
    return render(response, "main/home.html", {})

def pokemon(response):
    if response.method == "POST":
        form = Pokemon(response.POST)
        if form.is_valid():
            n = form.cleaned_data["nome"]
            p = getPokemon(n)
            p["form"] = form
        return render(response, "main/pokemon.html", p)
    else:
        form = Pokemon()
    return render(response, "main/pokemon.html", {"form":form})

