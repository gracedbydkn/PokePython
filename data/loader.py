import json
import random
from classes.pokemon import Pokemon
from classes.moves import Moves
from classes.local import Local

# Lê o arquivo JSON e retorna um dicionário de Pokémon indexado pelo nome.
def importarPokemons(caminho: str = "data/pokemons.json") -> dict[str, Pokemon]:
    with open(caminho, "r", encoding="utf-8") as f:
        dados = json.load(f)
    
    pokemons = {}
    for d in dados["pokemon"]:
        # Cria os objetos Moves para cada movimento listado no JSON.
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
# Lê o arquivo JSON e retorna um dicionário de locais indexado pelo nome,
# com os caminhos e Pokémon já vinculados aos objetos correspondentes.
def importarLocais(caminho: str = "data/locais.json", pokemons: dict[str, Pokemon] = None) -> dict[str, Local]:
    with open(caminho, "r", encoding="utf-8") as f:
        dados = json.load(f)

        locais = {}
        # Primeira passagem: cria todos os locais sem caminhos ainda.
        for d in dados["locais"]:
            pokemonRaw = d.get("pokemon")
            if isinstance(pokemonRaw, list):
                nomes = [p["nome"].strip() for p in pokemonRaw]
                pokemon = pokemons.get(random.choice(nomes)) if pokemons else None
            elif isinstance(pokemonRaw, str):
                pokemon = pokemons.get(pokemonRaw.strip()) if pokemons else None
            else:
                pokemon = None
                
            locais[d["nome"]] = Local(
                nome = d["nome"],
                caminhos = [],        
                pokemon = pokemon,
                isCura = d.get("isCura", False),
                titulo = d.get("titulo", [])
            )
        
        # Segunda passagem: vincula os caminhos entre locais já criados.
        for d in dados["locais"]:
            local = locais[d["nome"]]
            for destino_dict in d["caminhos"]:
                destino = locais.get(destino_dict["nome"])
                if destino:
                    local.caminhos.append(destino)
                else:
                    print(f"[AVISO] Caminho '{destino_dict['nome']}' não encontrado para '{d['nome']}'")

        return locais
