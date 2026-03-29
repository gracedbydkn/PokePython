from classes.moves import Moves
from assets.typechart import get_multiplicador

# Representa um Pokémon com seus atributos e comportamentos de batalha.
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

    # Executa um ataque contra o alvo e retorna dano causado, efetividade e efeito aplicado.
    def atacar(self, movimento, alvo: "Pokemon") -> dict:
        efetividade = get_multiplicador(movimento.tipo, alvo.tipo1, alvo.tipo2)
        if efetividade == 0:
            return {"dano": 0, "multiplicador": 0, "logEfeito": None}

        dano = alvo.receberDano(int(movimento.dano * efetividade * self.atkmulti)) 
        logEfeito = self.aplicarEfeito(movimento, alvo)

        return {"dano": dano, "multiplicador": efetividade, "logEfeito": logEfeito}
    
    # Aplica o efeito secundário do movimento (alterando ataque ou defesa) e retorna uma mensagem de log.
    def aplicarEfeito(self, movimento, inimigo: "Pokemon") -> str | None:
        if movimento.efeito is None:
            return None
        
        efeito = movimento.efeito
        alvo = self if efeito["alvo"] == "proprio" else inimigo # Efeito é aplicado no próprio Pokémon ou no Inimigo.

        if efeito["atributo"] == "atkmulti":
            alvo.atkmulti *= efeito["valor"]
            atributoLog = "O ataque"
        elif efeito["atributo"] == "defmulti":
            alvo.defmulti *= efeito["valor"]
            atributoLog = "A defesa"

        direcao = "subiu" if efeito["valor"] > 1 else "caiu"

        return f"{atributoLog} de {alvo.nome} {direcao}"
    
    # Desconta o dano recebido do HP, aplicando o multiplicador de defesa.
    def receberDano(self, dano: int) -> int:
        danoFinal = max(1, int((dano / self.defmulti)))
        self.hp = max(0, self.hp - danoFinal)
        return danoFinal
    
    # Restaura HP quando for usado no local de abrigo.
    def curar(self, quantidade: int):
        self.hp = min(self.hpmax, self.hp + quantidade)
    
    # Retorna o HP atual como proporção do HP máximo (Utilizado para as barras de vida).
    def porcentagem_hp(self):
        return self.hp / self.hpmax
    
    # Verifica se o Pokémon ainda está vivo.
    def isVivo(self) -> bool:
        return self.hp > 0