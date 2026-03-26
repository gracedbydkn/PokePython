from pokemon import Pokemon
from local import Local

class Jogador:
    def __init__(self, equipe: list[Pokemon], localAtual: Local):
        self.equipe = equipe
        self.localAtual = localAtual

    def mover(self, destino: Local) -> bool:
        if destino not in self.localAtual.caminhos:
            return False
        self.localAtual = destino
        return True

    def is_vivo(self) -> bool:
        return any(p.is_vivo() for p in self.equipe)

    def pokemonAtual(self) -> Pokemon:
        return next(p for p in self.equipe if p.is_vivo())