import json
from classes.pokemon import Pokemon
from classes.moves import Moves

def importarPokemons(caminho: str = "data/pokemons.json") -> dict[str, Pokemon]:
    with open(caminho, "r", encoding="utf-8") as f:
        dados = json.load(f)
    
    pokemons = {}
    for d in dados["pokemon"]:
        movimentos = [
            Moves(m["nome"], m["tipo"], m["dano"], m["efeito"])
            for m in d["movimentos"]
        ]
        pokemon = Pokemon(
            nome = d["nome"],
            tipo1 = d["tipo1"],
            tipo2 = d["tipo2"],
            hp = d["hp"],
            hpmax = d["hpmax"],
            movimentos = movimentos,
            atkmulti = d["atkmulti"],
            defmulti = d["defmulti"],
            ascii = d["ascii"]
        )
        pokemons[d["nome"]] = pokemon
    
    return pokemons