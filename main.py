from data.loader import importarPokemons
from classes.pokemon import Pokemon
from classes.moves import Moves

print(f"Escolha seu inicial: \n[1] Totodile   [2] Rowlet   [3] Chimchar")
inicial = input("")

totodilemoves1 = Moves("Pistola d'água", "agua", 10, None)
totodilemoves2 = Moves("Arranhão", "normal", 10, None)
totodilemoves3 = Moves("Encarada", "normal", 0, None)
totodilemoves4 = Moves("Mordida", "sombrio", 10, None)

if inicial == "1":
    totodile = Pokemon("Totodile", "agua", None, 18, 20, [totodilemoves1, totodilemoves2, totodilemoves3, totodilemoves4], None, None, None)

pokemons = importarPokemons()

rowlet = pokemons["Rowlet"]

print(totodile.tipo1, totodile.nome, totodile.hp)
print(rowlet.tipo1, rowlet.tipo2, rowlet.atkmulti)
