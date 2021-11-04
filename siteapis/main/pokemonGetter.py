import requests
from requests.api import request

def getPokemon(nome):
    try:
        response = requests.get("https://pokeapi.co/api/v2/pokemon/"+nome.lower()).json()
    except:
        pokemon = {"Nome": nome + " não encontrado/a"}
        return pokemon
    pokemon = {
        "Nome":response["name"].capitalize(),
        "Foto":response["sprites"]["front_default"],
        "Tipo":[],
        "Fraqueza":[],
        "Id":response["id"],
        "Stats":[]
    }
    for item in response["types"]:
        pokemon["Tipo"].append(tradTipo(item["type"]["name"]))
    for index, item in enumerate(response["stats"]):
        pokemon["Stats"].append(response["stats"][index]["base_stat"])
    
    temp = []
    for item in response["types"]:
        resp = requests.get(item["type"]["url"]).json()
        for i in resp["damage_relations"]["double_damage_from"]:
            temp.append(tradTipo(i["name"]))
    pokemon["Fraqueza"] = list(set(temp))
    return pokemon


def tradTipo(tipo):
    if tipo == "normal":
        return "Normal 👤"
    elif tipo == "fire":
        return "Fogo 🔥"
    elif tipo == "water":
        return "Água 💧"
    elif tipo == "grass":
        return "Grama 🥗"
    elif tipo == "electric":
        return "Elétrico ⚡"
    elif tipo == "ice":
        return "Gelo ❄"
    elif tipo == "fighting":
        return "Lutador 👊"
    elif tipo == "poison":
        return "Veneno 💀"
    elif tipo == "ground":
        return "Terrestre 🌎"
    elif tipo == "flying":
        return "Voador 🐤"
    elif tipo == "psychic":
        return "Psiquico 😵"
    elif tipo == "bug":
        return "Inseto 🦗"
    elif tipo == "rock":
        return "Pedra 🏔"
    elif tipo == "ghost":
        return "Fantasma 👻"
    elif tipo == "dark":
        return "Dark 🧛‍♀️"
    elif tipo == "dragon":
        return "Dragão 🐲"
    elif tipo == "steel":
        return "Aço 🔩"
    elif tipo == "fairy":
        return "Fada 🧚‍♂️"
    else:
        return tipo