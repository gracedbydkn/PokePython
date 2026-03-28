from classes.pokemon import Pokemon

class Local:
    def __init__(self, nome: str, caminhos: list["Local"], pokemon: Pokemon | None = None, isCura: bool = False):
        self.nome = nome
        self.pokemon = pokemon
        self.caminhos = caminhos
        self.isCura = isCura

    def curarEquipe(self, jogador) -> None:
        if not self.isCura:
            return
        for p in jogador.equipe:
            p.hp = p.hpmax