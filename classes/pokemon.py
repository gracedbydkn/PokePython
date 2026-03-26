from moves import Moves
from assets.typechart import get_multiplicador

class Pokemon:
    def __init__(self, nome: str, tipo1: str, tipo2: str | None, hp: int, hpmax: int, movimentos: list[Moves], atkmulti: float | None, defmulti: float | None, ascii):
        self.nome = nome
        self.tipo1 = tipo1
        self.tipo2 = tipo2
        self.hp = hp
        self.hpmax = hpmax
        self.movimentos = movimentos
        self.atkmulti = atkmulti if atkmulti is not None else 1
        self.defmulti = defmulti if defmulti is not None else 1
        self.ascii = ascii

    def atacar(self, movimento, inimigo) -> dict:
        efetividade = get_multiplicador(movimento.tipo, inimigo.tipo1, inimigo.tipo2)
        dano = inimigo.receber_dano(int(movimento.dano * efetividade * self.atkmulti)) 
        return {"dano": dano, "multiplicador": efetividade}
    
    def receber_dano(self, dano: int) -> int:
        dano_final = (dano / self.defmulti)
        self.hp = max(0, self.hp - dano_final)
        return dano_final
    
    def curar(self, quantidade: int):
        self.hp = min(self.hpmax, self.hp + quantidade)
    
    def porcentagem_hp(self):
        return self.hp / self.hpmax