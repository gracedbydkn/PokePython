import os
import random
import re
from itertools import zip_longest
from classes.pokemon import Pokemon
from classes.jogador import Jogador
from data.batalhasCounter import EVOLUCOES, DIALOGOS_VITORIA
from data.loader import importarPokemons
import time

# ── Cores ANSI ──
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

largura = 230

# Funções para centralizar e formatar o texto
def visibleLen(s: str) -> int:
    return len(re.sub(r'\033\[[0-9;]*m', '', s))

def padCenter(s: str, width: int) -> str:
    pad = width - visibleLen(s)
    left = pad // 2
    right = pad - left
    return ' ' * left + s + ' ' * right

def padLeft(s: str, width: int) -> str:
    pad = width - visibleLen(s)
    return s + ' ' * max(0, pad)
# -----

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

def exibirEstado(jogadorPokemon: Pokemon, inimigo: Pokemon, local = None):
    col = largura // 2

    print("\033[33m═\033[0m" * largura)
    if local and local.titulo:
        for linha in local.titulo:
            print(f"\033[33m{linha:^{largura}}\033[0m")
    else:
        nome = local.nome if local else ""
        print(f"\033[36m{'★  ' + nome.upper() + '  ★':^{largura}}\033[0m")
    print("\033[33m═\033[0m" * largura)
    print()

    nomeJogador = f"\033[32m{jogadorPokemon.nome}\033[0m"
    nomeInimigo = f"\033[91m{inimigo.nome}\033[0m"
    print(padCenter(nomeJogador, col) + padCenter(nomeInimigo, col))

    hpJogador = barraHP(jogadorPokemon.hp, jogadorPokemon.hpmax)
    hpInimigo = barraHP(inimigo.hp, inimigo.hpmax)
    hpJogadorStr = f"HP {hpJogador}"
    hpInimigoStr = f"HP {hpInimigo}"
    print(padCenter(hpJogadorStr, col) + padCenter(hpInimigoStr, col))

    print()
    print("\033[33m─\033[0m" * largura)
    
    linhasJogador = jogadorPokemon.ascii if jogadorPokemon.ascii else []
    linhasInimigo = inimigo.ascii if inimigo.ascii else []

    for lInimigo, lJogador in zip_longest(linhasInimigo, linhasJogador, fillvalue=""):
        print(padLeft(padCenter(lJogador, col), col) + padCenter(lInimigo, col))
    
    print()
    print("\033[33m─\033[0m" * largura)
    
def escolherAcao(jogador:Jogador)-> str:
    col = largura / 2
    temOutroVivo = any(
        p.isVivo() and p!=jogador.pokemonAtual()
        for p in jogador.equipe
    )

    titulo = f"O que {jogador.pokemonAtual().nome} vai fazer?"
    print(f"\n{padCenter(titulo, largura)}\n")
    print("─" * largura)

    opcao1 = f"[\033[33m1\033[0m] Atacar"
    opcao2 = f"[\033[33m2\033[0m] Trocar" if temOutroVivo else f"[2] Trocar (indisponível)"
    opcoes = padCenter(opcao1 + "      " + opcao2, largura)
    print(f"\n{opcoes}")

    while True:
        escolha = input(f"\n{"":^90}> ").strip()
        if escolha == "1":
            return"atacar"
        if escolha == "2" and temOutroVivo:
            return"trocar"
        erro = "Escolha inválida."
        print(padCenter(erro, largura))

def corTipo(tipo: str) -> str:
    return CORESTIPO.get(tipo.lower())

def escolherMovimento(pokemon:Pokemon):
    titulo = f"Qual ataque \033[33m{pokemon.nome}\033[0m vai utilizar?"
    print(f"\n{padCenter(titulo, largura)}\n")
    print("─" * largura)    

    for i, mov in enumerate(pokemon.movimentos):
        cor = corTipo(mov.tipo)
        linha = f"[\033[33m{i+1}\033[0m] {mov.nome:<24} {cor}{mov.tipo.upper():<10}{RESET}  Dano:{mov.dano:<4}"
        print(padCenter(linha, largura))

    voltar = "[\033[33m0\033[0m] Voltar"
    print(f"\n{padCenter(voltar, largura)}\n")
    

    while True:
        escolha = input("> ").strip()
        if escolha == "0":
            return None
        if escolha.isdigit() and 1 <= int(escolha) <= len(pokemon.movimentos):
            return pokemon.movimentos[int(escolha)-1]
        erro = "Escolha inválida."
        print(padCenter(erro, largura))


def escolherTroca(jogador: Jogador, inimigo: Pokemon, local = None) -> Pokemon:
    todos = jogador.equipe
    disponiveis = [p for p in todos if p.isVivo() and p != jogador.pokemonAtual()]
    
    limparTela()
    exibirEstado(jogador.pokemonAtual(), inimigo, local)
    titulo = "Trocar por qual Pokémon?"
    print(padCenter(titulo, largura))
    print(f"\033[33m─\033[0m" * largura)

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
            hud1 = f"\033[31m[✗]{RESET} \033[31m{p.nome:<16}{RESET}  {tipo_str}{padding}  \033[31mHP:{RESET} {barraHP(0, p.hpmax, tamanho=15)}\n"
            print(padCenter(hud1, largura))
            continue
        hud2 = f"[\033[33m{idx}{RESET}] {RESET}{p.nome:<16}{RESET}  {tipo_str}{padding}  {RESET}HP:{RESET} {barraHP(p.hp, p.hpmax, tamanho=15)}\n"
        print(padCenter(hud2, largura))
        idx += 1
    
    voltar = "[\033[33m0\033[0m] Voltar\n"
    print(padCenter(voltar, largura))

    while True: 
        escolha = input(" > ").strip()
        if escolha == "0":
            return None
        if escolha.isdigit() and 1 <= int(escolha) <= len(disponiveis):
            return disponiveis[int(escolha) - 1]
        erro = "Escolha inválida"
        print(padCenter(erro, largura))

def forcarTroca(jogador: Jogador, inimigo: Pokemon, local = None) -> bool:
    todos = jogador.equipe
    disponiveis = [p for p in todos if p.isVivo()]
    if not disponiveis:
        return False
    
    limparTela()
    exibirEstado(jogador.equipe[0], inimigo, local)
    desmaio = "Seu pokémon foi derrotado!"
    print(padCenter(desmaio, largura))
    print(f"\033[33m─\033[0m]" * largura)
    escolha = "Escolha seu próximo pokémon"
    print(padCenter(escolha, largura))

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
            hud1 = f"\n  \033[31m[✗]{RESET} \033[31m{p.nome:<16}{RESET}  {tipo_str}{padding}  \033[31mHP:{RESET} {barraHP(0, p.hpmax, tamanho=15)}"
            print(padCenter(hud1, largura))
            continue

        hud2 = f"\n  [\033[33m{idx}{RESET}] {RESET}{p.nome:<16}{RESET}  {tipo_str}{padding}  {RESET}HP:{RESET} {barraHP(p.hp, p.hpmax, tamanho=15)}"
        print(padCenter(hud2, largura))
        idx += 1

    print()
    while True:
        escolha = padCenter(input(" > ").strip(), largura)
        if escolha.isdigit() and 1 <= int(escolha) <= len(disponiveis):
            jogador.trocarPokemon(disponiveis[int(escolha) - 1])
            return True
        erro = (" Escolha inválida.")
        print(padCenter(erro, largura))

def exibirLog(atacante: str, movimentoNome: str, resultado: dict):
    log = f"{atacante} utilizou {movimentoNome}!"
    print(padCenter(log, largura))
    
    if resultado["multiplicador"] == 0:
        multi = f"\033[91m  ⛒ ⛒ {RESET} O alvo é imune!\033[91m ⛒ ⛒  {RESET}\n"
        print(padCenter(multi, largura))
    elif resultado["multiplicador"] < 1:
        multi = f"\033[31m ✗✗ {RESET} Não é muito efetivo...\033[31m ✗✗ {RESET}"
        print(padCenter(multi, largura))
    elif resultado["multiplicador"] > 1:
        multi = f"\033[33m ★★ {RESET} É super efetivo!\033[33m ★★ {RESET}"
        print(padCenter(multi, largura))

    if resultado["dano"] > 0:
        dano = f"Causou {resultado['dano']} de dano.\n"
        print(padCenter(dano, largura))

    if resultado["logEfeito"]:
        print(padCenter(resultado["logEfeito"], largura))
    

def turnoInimigo(inimigo: Pokemon, alvo: Pokemon):
    movimento = random.choice(inimigo.movimentos)
    resultado= inimigo.atacar(movimento, alvo)
    exibirLog(inimigo.nome, movimento.nome, resultado)
    
def verificarEvolucao(jogador: Jogador, pokemons: dict):
    pokemon = jogador.inicial
    evolucao = EVOLUCOES.get(pokemon.nome)

    if not evolucao:
        return
    if jogador.batalhas != evolucao["batalhas"]:
        return
    novoNome = evolucao["evolucao"]
    novo = pokemons.get(novoNome)
    if not novo:
        return
    evo1 = f"{Y}Espera... algo está acontecendo com {pokemon.nome}!{RESET}\n"
    print(padCenter(evo1, largura))
    enter = f"Pressione Enter...\n"
    print(padCenter(enter, largura))

    idx = jogador.equipe.index(pokemon)
    novo.hp = novo.hpmax
    jogador.equipe[idx] = novo
    jogador.inicial = novo

    evo2 = f"{Y}★ {pokemon.nome} evoluiu para {novo.nome}! ★{RESET}\n"
    print(padCenter(evo2, largura))

def telaVitoria(inimigo: Pokemon, jogador: Jogador, pokemons: dict):
    derrota =f"{inimigo.nome} foi derrotado!"
    print(padCenter(derrota, largura))
    dialogo = DIALOGOS_VITORIA.get(jogador.batalhas, [])
    print()
    for linha in dialogo:
        dialogo = f"  {inimigo.nome}: \"{linha}\""
        print(padCenter(dialogo, largura))
    
    jogador.batalhas += 1
    jogador.recrutar(inimigo)
    recrutar = f"{inimigo.nome} se juntou à sua equipe!\n"
    print(padCenter(recrutar, largura))

    verificarEvolucao(jogador, pokemons)
    confirmar = f"\033[33mPressione Enter para continuar...\033[0m"
    input(padCenter(confirmar, largura))

def telaDerrota():
    derrota = "\nVocê foi derrotado..."
    print(padCenter(derrota, largura))
    sair = "[1] Sair"
    print(padCenter(sair,largura))
    print(" > ")
    exit()

def iniciarBatalha(jogador: Jogador, inimigo: Pokemon, local=None, pokemons: dict = {}):
    while True:
        limparTela()
        exibirEstado(jogador.pokemonAtual(), inimigo, local)
        
        acao = escolherAcao(jogador)

        if acao == "trocar":
            novo = escolherTroca(jogador, inimigo, local)
            if novo is None:
                continue
            jogador.trocarPokemon(novo)
            novopokemon = f"Vai, {novo.nome}!\n"
            print(padCenter(novopokemon, largura))
            turnoInimigo(inimigo, jogador.pokemonAtual())
        else:
            movimento = escolherMovimento(jogador.pokemonAtual())
            if movimento is None:
                continue

            resultado = jogador.pokemonAtual().atacar(movimento, inimigo)
            exibirLog(jogador.pokemonAtual().nome, movimento.nome, resultado)
            if not inimigo.isVivo():
                limparTela()
                exibirEstado(jogador.pokemonAtual(), inimigo, local)
                telaVitoria(inimigo, jogador, pokemons)
                return "vitoria"
        
            turnoInimigo(inimigo, jogador.pokemonAtual())

        if not jogador.equipe[0].isVivo():
            if not jogador.isVivo():
                limparTela()
                exibirEstado(jogador.equipe[0], inimigo, local)
                telaDerrota()
                return "derrota"
            forcarTroca(jogador, inimigo, local)
            continue


        if not jogador.isVivo():
            limparTela()
            exibirEstado(jogador.pokemonAtual(), inimigo, local)
            telaDerrota()
            return "derrota"

        confirmar = "Pressione Enter para continuar..."
        input(padCenter(confirmar, largura))