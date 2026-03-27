from classes.pokemon import Pokemon
from classes.local import Local

class Jogador:
    def __init__(self, equipe: list[Pokemon], localAtual: Local):
        self.equipe = equipe
        self.localAtual = localAtual

    def mover(self, destino: Local) -> bool:
        if destino not in self.localAtual.caminhos:
            return False
        self.localAtual = destino
        return True

    def isVivo(self) -> bool:
        return any(p.isVivo() for p in self.equipe)

    def pokemonAtual(self) -> Pokemon:
        return next(p for p in self.equipe if p.isVivo())
    
    def trocarPokemon(self, novo: Pokemon) -> bool:
        if novo not in self.equipe:
            return False
        if not novo.isVivo():
            return False
        if novo == self.pokemonAtual():
            return False
        self.equipe.remove(novo)
        self.equipe.insert(0, novo)
        return True

    def recrutar(self, pokemon: Pokemon) -> bool:
        pokemon.hp = pokemon.hpmax
        self.equipe.append(pokemon)
        return True