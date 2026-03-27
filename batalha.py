import os
import random
from itertools import zip_longest
from classes.pokemon import Pokemon
from classes.jogador import Jogador

RESET = "\033[0m"
V  = "\033[92m"
R  = "\033[31m"
Y  = "\033[33m"
V2 = "\033[102m"
V2 = "\033[32m"

CORESTIPO = {
    "normal":   "\033[97m",   # branco
    "fogo":     "\033[31m",   # vermelho
    "agua":     "\033[94m",   # azul
    "grama":    "\033[32m",   # verde escuro
    "eletrico": "\033[93m",   # amarelo claro
    "gelo":     "\033[96m",   # ciano
    "lutador":  "\033[91m",   # vermelho pastel
    "veneno":   "\033[35m",   # roxo escuro
    "terra":    "\033[33m",   # amarelo escuro
    "voador":   "\033[36m",   # ciano escuro
    "psiquico": "\033[95m",   # magenta
    "inseto":   "\033[92m",   # verde claro
    "pedra":    "\033[33m",   # amarelo escuro
    "fantasma": "\033[90m",   # cinza escuro
    "dragao":   "\033[34m",   # azul escuro
    "sombrio":  "\033[90m",   # cinza escuro
    "aço":      "\033[37m",   # cinza claro
    "fada":     "\033[95m"    # magenta
}


def limparTela():
    os.system('cls' if os.name == 'nt' else 'clear')

def barraHP(hp, hpMax, tamanho=20):
    if hpMax == 0:
        return f"[{'█' * tamanho}] 0/0"
    proporcao = hp/hpMax
    preenchido = int(proporcao * tamanho)
    vazio = tamanho - preenchido

    if proporcao > 0.5:
        cor = V
    elif proporcao > 0.25:
        cor = Y
    else:
        cor = R

    barra = f"{cor}{'█' * preenchido}{RESET}{'░' * vazio}"

    return f"[{barra}] {hp}/{hpMax}"

def exibirEstado(jogadorPokemon: Pokemon, inimigo: Pokemon):
    
    largura = 124
 
    nomeJogador = f"                        {jogadorPokemon.nome}"
    hpJogador =   f"              HP {barraHP(jogadorPokemon.hp, jogadorPokemon.hpmax)}"
    nomeInimigo = f"                           {inimigo.nome}"
    hpInimigo =   f"                        HP {barraHP(inimigo.hp, inimigo.hpmax)}"

    col = largura // 2
    print("\033[33m═\033[0m" * largura)
    print(f"\033[36m{'★  BATALHA POKÉMON  ★':^{largura}}\033[0m")
    print("\033[33m═\033[0m" * largura)
    print()
    print(f"\033[32m{nomeJogador:<{col}}\033[91m{nomeInimigo}\033[0m")
    print(f"{hpJogador:<{col}}{hpInimigo}")
    print()
    print("─" * largura)

    linhasInimigo = inimigo.ascii if inimigo.ascii else []
    linhasJogador = jogadorPokemon.ascii if jogadorPokemon.ascii else []

    for lInimigo, lJogador in zip_longest(linhasInimigo, linhasJogador, fillvalue=""):
        print(f"{lJogador:<{col}}{lInimigo}")
    
    print()
    print("─" * largura)
    
def escolherAcao(jogador:Jogador)-> str:
    temOutroVivo = any(
        p.isVivo() and p!=jogador.pokemonAtual()
        for p in jogador.equipe
    )

    print(f"  O que {jogador.pokemonAtual().nome} vai fazer?")
    print("─" * 124)
    print("  [\033[33m1\033[0m] Atacar", end = "")
    print("  [\033[33m2\033[0m] Trocar" if temOutroVivo else "  [2] Trocar (indispoível)")

    while True:
        escolha = input("\n  > ").strip()
        if escolha == "1":
            return"atacar"
        if escolha == "2" and temOutroVivo:
            return"trocar"
        print("  Escolha inválida.")

def corTipo(tipo: str) -> str:
    return CORESTIPO.get(tipo.lower())

def escolherMovimento(pokemon:Pokemon):
    print(f"\n  Qual ataque \033[33m{pokemon.nome}\033[0m vai utilizar?")
    print("─" * 124)    
    for i, mov in enumerate(pokemon.movimentos):
        cor = corTipo(mov.tipo)
        print(f"  [\033[33m{i+1}\033[0m] {mov.nome:<24} {cor}{mov.tipo.upper():<10}{RESET}  Dano:{mov.dano:<4}")
    print("\n  [\033[33m0\033[0m] Voltar\n")

    while True:
        escolha = input("  > ").strip()
        if escolha == "0":
            return None
        if escolha.isdigit() and 1 <= int(escolha) <= len(pokemon.movimentos):
            return pokemon.movimentos[int(escolha)-1]
        print("  Escolha inválida.")


def escolherTroca(jogador: Jogador) -> Pokemon:
    disponiveis = [p for p in jogador.equipe if p.isVivo() and p != jogador.pokemonAtual()]
    print("\nEscolha um companheiro:")
    for i, p in enumerate(disponiveis):
        print(f"[{i+1}] {p.nome}  HP: {p.hp}/{p.hpmax}")

    while True:
        escolha = input("> ").strip()
        if escolha.isdigit() and 1 <= int(escolha) <= len(disponiveis):
            return disponiveis[int(escolha) - 1]
        print("Escolha inválida")

def exibirLog(atacante: str, movimentoNome: str, resultado: dict):
    print(f"\n{atacante} utilizou {movimentoNome}!")
    
    if resultado["multiplicador"] == 0:
        print("🚫 O alvo é imune!")
    elif resultado["multiplicador"] < 1:
        print("❌ Não é muito efetivo...")
    elif resultado["multiplicador"] > 1:
        print("⭐ É super efetivo!")

    if resultado["dano"] > 0:
        print(f"Causou {resultado['dano']} de dano.")

    if resultado["logEfeito"]:
        print(resultado["logEfeito"]) 
    

def turnoInimigo(inimigo: Pokemon, alvo: Pokemon):
    movimento = random.choice(inimigo.movimentos)
    resultado= inimigo.atacar(movimento, alvo)
    exibirLog(inimigo.nome, movimento.nome, resultado)
    
def telaVitoria(inimigo: Pokemon, jogador: Jogador):
    print(f"\n{inimigo.nome} foi derrotado!")
    # dialogo e recrutamento
    jogador.recrutar(inimigo)
    print(f"{inimigo.nome} se juntou à sua equipe!")

def telaDerrota():
    print("\nVocê foi derrotado...")
    print("[1] Sair")
    input("> ")
    exit()

def iniciarBatalha(jogador: Jogador, inimigo: Pokemon):
    while True:
        limparTela()
        exibirEstado(jogador.pokemonAtual(), inimigo)
        
        acao = escolherAcao(jogador)

        if acao == "trocar":
            novo = escolherTroca(jogador)
            jogador.trocarPokemon(novo)
            print(f"Vai, {novo.nome}!")
            turnoInimigo(inimigo, jogador.pokemonAtual())
        else:
            movimento = escolherMovimento(jogador.pokemonAtual())
            if movimento is None:
                continue

            resultado = jogador.pokemonAtual().atacar(movimento, inimigo)
            exibirLog(jogador.pokemonAtual().nome, movimento.nome, resultado)
            if not inimigo.isVivo():
                limparTela()
                exibirEstado(jogador.pokemonAtual(), inimigo)
                telaVitoria(inimigo, jogador)
                return "vitoria"
        
            turnoInimigo(inimigo, jogador.pokemonAtual())

        if not jogador.isVivo():
            limparTela()
            exibirEstado(jogador.pokemonAtual(), inimigo)
            telaDerrota()
            return "derrota"

        input("\nPressione Enter para continuar...")