from classes.pokemon import Pokemon
from classes.local import Local

# Representa o jogador, sua equipe de Pokémon e sua posição no mapa.
class Jogador:
    def __init__(self, equipe: list[Pokemon], localAtual: Local):
        self.equipe = equipe
        self.localAtual = localAtual
        self.batalhas = 0            # Contador de batalhas.
        self.inicial = equipe[0]     # Armazena o Pokémon inicial.

    # Move o jogador para um local destino; retorna False se o destino não for um caminho válido.
    def mover(self, destino: Local) -> bool:
        if destino not in self.localAtual.caminhos:
            return False
        self.localAtual = destino
        return True

    # Retorna True se ao menos um Pokémon da equipe ainda estiver vivo.
    def isVivo(self) -> bool:
        return any(p.isVivo() for p in self.equipe)

    # Retorna o primeiro Pokémon vivo da equipe (considerado o Pokémon atual).
    def pokemonAtual(self) -> Pokemon:
        vivos = [p for p in self.equipe if p.isVivo()]
        return vivos[0]
    
    # Move o Pokémon escolhido para o primeiro da equipe, tornando o ativo.
    def trocarPokemon(self, novo: Pokemon) -> bool:
        if novo not in self.equipe:
            return False
        if not novo.isVivo():       # Não pode trocar para um Pokémon desmaiado.
            return False
        if novo == self.pokemonAtual(): # Já é o Pokémon atual.
            return False
        self.equipe.remove(novo)
        self.equipe.insert(0, novo)
        return True

    # Adiciona um Pokémon recrutado à equipe com HP totalmente restaurado.
    def recrutar(self, pokemon: Pokemon) -> bool:
        pokemon.hp = pokemon.hpmax
        self.equipe.append(pokemon)
        return True