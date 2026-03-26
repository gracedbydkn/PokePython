from pokemon import Pokemon

class Local:
    def __init__(self, nome: str, caminhos: list["Local"], pokemon: Pokemon | None = None, is_cura: bool = False):
        self.nome = nome
        self.pokemon = pokemon
        self.caminhos = caminhos
        self.is_cura = is_cura