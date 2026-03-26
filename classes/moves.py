class Moves:
    def __init__(self, nome: str, tipo: str, dano: int, efeito: str | None = None):
        self.nome = nome
        self. tipo = tipo
        self.dano = dano
        self.efeito = efeito