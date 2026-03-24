from moves import Moves

class Pokemon:
    def __init__(self, nome: str, tipo1: str, tipo2: str | None, hp: int, movimentos: Moves, efeitos: str | None, ascii):
        self.nome = nome
        self.tipo1 = tipo1
        self.tipo2 = tipo2
        self.hp = hp
        self.movimentos = movimentos
        self.efeitos = efeitos | None = efeitos 
        self.ascii = ascii