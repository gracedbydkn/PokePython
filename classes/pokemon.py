from classes.moves import Moves
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

    def atacar(self, movimento, alvo: "Pokemon") -> dict:
        efetividade = get_multiplicador(movimento.tipo, alvo.tipo1, alvo.tipo2)
        dano = alvo.receberDano(int(movimento.dano * efetividade * self.atkmulti)) 
        logEfeito = self.aplicarEfeito(movimento, alvo)

        return {"dano": dano, "multiplicador": efetividade, "logEfeito": logEfeito}
    
    def aplicarEfeito(self, movimento, inimigo: "Pokemon") -> str | None:
        if movimento.efeito is None:
            return None
        
        efeito = movimento.efeito
        alvo = self if efeito["alvo"] == "proprio" else inimigo

        if efeito["atributo"] == "atkmulti":
            alvo.atkmulti *= efeito["valor"]
            atributoLog = "O ataque"
        elif efeito["atributo"] == "defmulti":
            alvo.defmulti *= efeito["valor"]
            atributoLog = "A defesa"

        direcao = "subiu" if efeito["valor"] > 1 else "caiu"

        return f"{atributoLog} de {alvo.nome} {direcao}"
    
    def receberDano(self, dano: int) -> int:
        danoFinal = max(1, int((dano / self.defmulti)))
        self.hp = max(0, self.hp - danoFinal)
        return danoFinal
    
    def curar(self, quantidade: int):
        self.hp = min(self.hpmax, self.hp + quantidade)
    
    def porcentagem_hp(self):
        return self.hp / self.hpmax
    
    def isVivo(self) -> bool:
        return self.hp > 0