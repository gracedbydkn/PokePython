from classes.pokemon import Pokemon

# Representa um local do mapa que o jogador pode explorar.
class Local:
    def __init__(self, nome: str, caminhos: list["Local"], pokemon: Pokemon | None = None, isCura: bool = False, titulo: list[str] | None = None):
        self.nome = nome
        self.pokemon = pokemon    # Pokémon selvagem presente no local; None se não houver.
        self.caminhos = caminhos  # Lista de locais conectados que o jogador pode acessar.
        self.isCura = isCura      # Indica se o local cura a equipe ao ser visitado.
        self.visitado = False     # Flag do local visitado.
        self.titulo = titulo if titulo is not None else []

    # Cura o HP de todos os Pokémon da equipe do jogador, se o local for de cura.
    def curarEquipe(self, jogador) -> None:
        if not self.isCura:
            return
        for p in jogador.equipe:
            p.hp = p.hpmax