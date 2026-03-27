from classes.pokemon import Pokemon

class Local:
    def __init__(self, nome: str, caminhos: list["Local"], pokemon: Pokemon | None = None, isCura: bool = False):
        self.nome = nome
        self.pokemon = pokemon
        self.caminhos = caminhos
        self.isCura = isCura