import json
from classes.pokemon import Pokemon
from classes.moves import Moves
from classes.local import Local

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

def importarLocais(caminho: str = "data/locais.json", pokemons: dict[str, Pokemon] = None) -> dict[str, Local]:
    with open(caminho, "r", encoding="utf-8") as f:
        dados = json.load(f)
        print(type(dados))
        print(type(dados["locais"]))
        print(dados["locais"][0])

        locais = {}
        for d in dados["locais"]:
            nomePokemon = d["pokemon"].strip() if isinstance(d["pokemon"], str) else None
            pokemon = pokemons.get(nomePokemon) if (pokemons and nomePokemon) else None

            locais[d["nome"]] = Local(
                nome = d["nome"],
                caminhos = [],        
                pokemon = pokemon,
                isCura = d.get("isCura", False)
            )
        
        for d in dados["locais"]:
            local = locais[d["nome"]]
            for destino_dict in d["caminhos"]:
                destino = locais.get(destino_dict["nome"])
                if destino:
                    local.caminhos.append(destino)
                else:
                    print(f"[AVISO] Caminho '{destino_dict['nome']}' não encontrado para '{d['nome']}'")

        return locais
