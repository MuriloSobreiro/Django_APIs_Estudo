import requests
from requests.api import request

def getPokemon(nome):
    try:
        response = requests.get("https://pokeapi.co/api/v2/pokemon/"+nome.lower()).json()
    except:
        pokemon = {"Nome": nome + " nÃ£o encontrado/a"}
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
        return "Normal ð¤"
    elif tipo == "fire":
        return "Fogo ð¥"
    elif tipo == "water":
        return "Ãgua ð§"
    elif tipo == "grass":
        return "Grama ð¥"
    elif tipo == "electric":
        return "ElÃ©trico â¡"
    elif tipo == "ice":
        return "Gelo â"
    elif tipo == "fighting":
        return "Lutador ð"
    elif tipo == "poison":
        return "Veneno ð"
    elif tipo == "ground":
        return "Terrestre ð"
    elif tipo == "flying":
        return "Voador ð¤"
    elif tipo == "psychic":
        return "Psiquico ðµ"
    elif tipo == "bug":
        return "Inseto ð¦"
    elif tipo == "rock":
        return "Pedra ð"
    elif tipo == "ghost":
        return "Fantasma ð»"
    elif tipo == "dark":
        return "Dark ð§ââï¸"
    elif tipo == "dragon":
        return "DragÃ£o ð²"
    elif tipo == "steel":
        return "AÃ§o ð©"
    elif tipo == "fairy":
        return "Fada ð§ââï¸"
    else:
        return tipo