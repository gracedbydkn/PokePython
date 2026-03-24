from pokemon import Pokemon

class Moves:
    def __init__(self, nome: str, pokemon:Pokemon, tipo: str, dano: int, efeito: str | None):
        self.nome = nome
        self.pokemon = pokemon
        self. tipo = tipo
        self.dano = dano
        self.efeito = efeito | None = efeito
        