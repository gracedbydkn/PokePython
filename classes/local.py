from pokemon import Pokemon

class Local:
    def __init__(self, nome: str, pokemon: Pokemon, caminhos: Local):
        self.nome = nome
        self.pokemon = pokemon
        self.caminhos = caminhos