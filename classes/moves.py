# Representa um movimento e os atributos que ele possui.
class Moves:
    def __init__(self, nome: str, tipo: str, dano: int, efeito: dict | None = None):
        self.nome = nome
        self.tipo = tipo
        self.dano = dano
        self.efeito = efeito