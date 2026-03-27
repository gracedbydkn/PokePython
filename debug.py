from data.loader import importarPokemons
from classes.jogador import Jogador
from classes.local import Local
import batalha

pokemons = importarPokemons()

equipe = [pokemons["Lugia"], pokemons["Rayquaza"], pokemons["Groudon"], pokemons["Rowlet"]]

local_teste = Local("Teste", caminhos=[], pokemon=pokemons["Lugia"])
jogador = Jogador(equipe=equipe, localAtual=local_teste)

batalha.iniciarBatalha(jogador, local_teste.pokemon)