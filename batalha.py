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

def exibirEstado(jogadorPokemon: Pokemon, inimigo: Pokemon, nomeLocal: str = ""):
    largura = 124
 
    nomeJogador = f"                        {jogadorPokemon.nome}"
    hpJogador =   f"              HP {barraHP(jogadorPokemon.hp, jogadorPokemon.hpmax)}"
    nomeInimigo = f"                           {inimigo.nome}"
    hpInimigo =   f"                        HP {barraHP(inimigo.hp, inimigo.hpmax)}"

    col = largura // 2
    print("\033[33m═\033[0m" * largura)
    print(f"\033[36m{'★  ' + nomeLocal.upper() + '  ★':^{largura}}\033[0m")
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


def escolherTroca(jogador: Jogador, inimigo: Pokemon, nomeLocal: str = "") -> Pokemon:
    todos = jogador.equipe
    disponiveis = [p for p in todos if p.isVivo() and p != jogador.pokemonAtual()]
    
    limparTela()
    exibirEstado(jogador.pokemonAtual(), inimigo, nomeLocal)
    print(f" Trocar por qual Pokémon?")
    print("─" * 124)

    idx = 1
    for p in todos:
        if p == jogador.equipe[0]:
            continue
        
        LARGURA_TIPO = 22
        if p.tipo2:
            textoTipo = f"{p.tipo1.upper()} / {p.tipo2.upper()}"
            tipo_str = f"[ {corTipo(p.tipo1)}{p.tipo1.upper()}{RESET} / {corTipo(p.tipo2)}{p.tipo2.upper()}{RESET} ]"
        else:
            textoTipo = f"{p.tipo1.upper()}"
            tipo_str = f"[ {corTipo(p.tipo1)}{p.tipo1.upper()}{RESET} ]"

        padding = " " * (LARGURA_TIPO - len(textoTipo) - 2)

        if not p.isVivo():
            print(f"\n  \033[31m[✗]{RESET} \033[31m{p.nome:<16}{RESET}  {tipo_str}{padding}  \033[31mHP:{RESET} {barraHP(0, p.hpmax, tamanho=15)}")
            continue

        print(f"\n  [\033[33m{idx}{RESET}] {RESET}{p.nome:<16}{RESET}  {tipo_str}{padding}  {RESET}HP:{RESET} {barraHP(p.hp, p.hpmax, tamanho=15)}")
        idx += 1

    print(f"\n  [\033[33m0\033[0m] Voltar\n")

    while True: 
        escolha = input("> ").strip()
        if escolha == "0":
            return None
        if escolha.isdigit() and 1 <= int(escolha) <= len(disponiveis):
            return disponiveis[int(escolha) - 1]
        print("Escolha inválida")

def forcarTroca(jogador: Jogador, inimigo: Pokemon, nomeLocal: str = "") -> bool:
    todos = jogador.equipe
    disponiveis = [p for p in todos if p.isVivo()]
    if not disponiveis:
        return False
    
    limparTela()
    exibirEstado(jogador.equipe[0], inimigo, nomeLocal)

    print("  Seu pokémon foi derrotado!")
    print("─" * 124)
    print("  Escolha seu próximo pokémon:")

    idx = 1
    for p in todos:
        LARGURA_TIPO = 22
        if p.tipo2:
            textoTipo = f"{p.tipo1.upper()} / {p.tipo2.upper()}"
            tipo_str = f"[ {corTipo(p.tipo1)}{p.tipo1.upper()}{RESET} / {corTipo(p.tipo2)}{p.tipo2.upper()}{RESET} ]"
        else:
            textoTipo = f"{p.tipo1.upper()}"
            tipo_str = f"[ {corTipo(p.tipo1)}{p.tipo1.upper()}{RESET} ]"

        padding = " " * (LARGURA_TIPO - len(textoTipo) - 2)

        if not p.isVivo():
            print(f"\n  \033[31m[✗]{RESET} \033[31m{p.nome:<16}{RESET}  {tipo_str}{padding}  \033[31mHP:{RESET} {barraHP(0, p.hpmax, tamanho=15)}")
            continue

        print(f"\n  [\033[33m{idx}{RESET}] {RESET}{p.nome:<16}{RESET}  {tipo_str}{padding}  {RESET}HP:{RESET} {barraHP(p.hp, p.hpmax, tamanho=15)}")
        idx += 1

    print()
    while True:
        escolha = input(" > ").strip()
        if escolha.isdigit() and 1 <= int(escolha) <= len(disponiveis):
            jogador.trocarPokemon(disponiveis[int(escolha) - 1])
            return True
        print(" Escolha inválida.")

def exibirLog(atacante: str, movimentoNome: str, resultado: dict):
    print(f"\n{atacante} utilizou {movimentoNome}!")
    
    if resultado["multiplicador"] == 0:
        print(f"\033[91m  ⛒ ⛒ {RESET} O alvo é imune!\033[91m ⛒ ⛒  {RESET}")
    elif resultado["multiplicador"] < 1:
        print(f"\033[31m ✗✗ {RESET} Não é muito efetivo...\033[31m ✗✗ {RESET}")
    elif resultado["multiplicador"] > 1:
        print(f"\033[33m ★★ {RESET} É super efetivo!\033[33m ★★ {RESET}")

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

def iniciarBatalha(jogador: Jogador, inimigo: Pokemon, nomeLocal: str = ""):
    while True:
        limparTela()
        exibirEstado(jogador.pokemonAtual(), inimigo, nomeLocal)
        
        acao = escolherAcao(jogador)

        if acao == "trocar":
            novo = escolherTroca(jogador, inimigo, nomeLocal)
            if novo is None:
                continue
            jogador.trocarPokemon(novo)
            print(f"\nVai, {novo.nome}!")
            turnoInimigo(inimigo, jogador.pokemonAtual())
        else:
            movimento = escolherMovimento(jogador.pokemonAtual())
            if movimento is None:
                continue

            resultado = jogador.pokemonAtual().atacar(movimento, inimigo)
            exibirLog(jogador.pokemonAtual().nome, movimento.nome, resultado)
            if not inimigo.isVivo():
                limparTela()
                exibirEstado(jogador.pokemonAtual(), inimigo, nomeLocal)
                telaVitoria(inimigo, jogador)
                return "vitoria"
        
            turnoInimigo(inimigo, jogador.pokemonAtual())

        if not jogador.equipe[0].isVivo():
            if not jogador.isVivo():
                limparTela()
                exibirEstado(jogador.equipe[0], inimigo, nomeLocal)
                telaDerrota()
                return "derrota"
            forcarTroca(jogador, inimigo, nomeLocal)
            continue


        if not jogador.isVivo():
            limparTela()
            exibirEstado(jogador.pokemonAtual(), inimigo, nomeLocal)
            telaDerrota()
            return "derrota"

        input("\nPressione Enter para continuar...")