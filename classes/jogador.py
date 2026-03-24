from pokemon import Pokemon
from local import Local

class Jogador:
    def __init__(self, equipe: Pokemon, localAtual: Local):
        self.equipe = equipe
        self.localAtual = localAtual