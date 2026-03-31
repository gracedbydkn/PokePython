# Feito por:
# Gustavo Santana Coutinho Silva dos Reis - RA: 824144932
# Márcio Almeida Barrocal - RA: 824137249
# Gabriela Danielly Nascimento - RA: 82414637

from data.loader import importarPokemons, importarLocais
from classes.jogador import Jogador
from classes.local import Local
from menu import exibirCentralizado
import re
import batalha
import menu
import time
import sys
from scripts.gerar_titulos import LETRAS
from menu import LOGO

largura = 230

V = "\033[32m"
RESET = "\033[0m"

CURA = [
"\n",
V+"    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣤⣤⣤⣤⣤⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀",
V+"    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀",
V+"    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀ ⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣶⣶⣶⣶⣶⣶⣶⠀⠀⠀⠀⠀⠀⠀⠀⠀",
V+"    ⠀⠀⠀⠀⠀⠀⠀⣴⣶⣶⣶⣶⣾⣿⣿⣿⣿⣿⣷⣶⣶⣶⣶⣦⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀",
V+"    ⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀",
V+"    ⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀",
V+"    ⠀⠀⠀⠀⠀⠀⠀⠙⠛⠛⠛⠻⣿⣿⣿⣿⣿⣿⡿⠛⠛⠛⠛⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷",
V+"    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿",
V+"    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢿⣿⣿⣿⣿⡿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿",
V+"     ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠛⠛⠛⠛⠛⠛⣿⣿⣿⣿⣿⣿⣿⡟⠛⠛⠛⠛⠛⠛⠛⠛",
V+"    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣀⣀⣀⣀⣀⣀⣀⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀",
V+"    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀ ⠀⠀⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀",
V+"    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠸⣿⣿⣿⣿⣿⣿⠇⠀⠀⠀⠀⠀⠀⠀⠀",
V+"    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀",
V+"    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀",
V+"    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀",
V+"    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀",
V+"    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀",
V+"    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀",
V+"    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀",
V+"    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀",
V+"    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀",
V+"    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀",
V+"    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀",
V+"    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀",
V+"    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀",
V+"    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠛⠛⠛⠛⠛⠛⠛⠛⠛⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀",
V+"⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀"+RESET
]

def digitar(texto, delay=0.03):
    stripped = texto.strip(' ')
    espacoEsquerda = len(texto) - len(texto.lstrip(' '))
    espacoDireita = len(texto) - len(texto.rstrip(' '))

    sys.stdout.write(' ' * espacoEsquerda)
    sys.stdout.flush()

    for ch in stripped:
        sys.stdout.write(ch)
        sys.stdout.flush()
        time.sleep(delay)

    sys.stdout.write(' ' * espacoDireita)
    sys.stdout.flush()

def printASCII(palavra, delayLetra=0.4, delayLinha=0.03):
    palavra = palavra.upper()
    num_linhas = 6

    for linha in range(num_linhas):
        linha_texto = ""
        for char in palavra:
            if char in LETRAS:
                linha_texto += LETRAS[char][linha] + "  "
            else:
                linha_texto += "         "

        linhaCentralizada = padCenter(linha_texto, largura)
        digitar(linhaCentralizada, delay=delayLinha)
        sys.stdout.write('\n')
        sys.stdout.flush()
        time.sleep(delayLetra)

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

def exibirCabecalhoLocal(local):
    print("\033[33m═\033[0m" * largura)
    if local.titulo:
        for linha in local.titulo:
            print(f"\033[33m{linha:^{largura}}\033[0m")
    else:
        nome = local.nome if local else ""
        print(f"\033[36m{'★  ' + nome.upper() + '  ★':^{largura}}\033[0m")
    print("\033[33m═\033[0m" * largura)

def telaExploracao(jogador: Jogador, pokemons: dict):
    while True:
        local = jogador.localAtual

        if local.isCura:
            menu.limparTela()
            exibirCabecalhoLocal(local)
            print()
            for linha in CURA: 
                print(padCenter(linha, largura))
            cura = f"Sua equipe foi totalmente curada!"
            print(padCenter(cura, largura))
            local.curarEquipe(jogador)
            continuar = f"{menu.Y}Pressione Enter para continuar...{menu.RESET}"
            input(padCenter(continuar, largura))
        
        elif local.pokemon and local.pokemon.isVivo() and not local.visitado:
            resultado = batalha.iniciarBatalha(jogador, local.pokemon, local, pokemons)
            if resultado == "derrota":
                return "derrota"
            local.visitado = True
            continue

        if not local.caminhos:
            return "fim"
        
        menu.limparTela()
        exibirCabecalhoLocal(local)
        print()
        pergunta = f"Para onde você deseja ir?"
        print(padCenter(pergunta, largura))
        print()

        for i, caminho in enumerate(local.caminhos, 1):
            opcoes = f"[{menu.Y}{i}{menu.RESET}] {caminho.nome}"
            print(padCenter(opcoes, largura))
            print()
        print()
        print("\033[33m─\033[0m" * largura)

        while True:
            escolha = input(f"\n  {menu.Y}>{menu.RESET} ").strip()
            if escolha.isdigit() and 1 <= int(escolha) <= len(local.caminhos):
                jogador.mover(local.caminhos[int(escolha) - 1])
                break
            erro = "Escolha inválida"
            print(padCenter(erro, largura))

def main():
    pokemons = importarPokemons()
    locais = importarLocais(pokemons=pokemons)


    while True:
        menu.exibirMenu()
        escolha = input("\n  > ").strip()

        if escolha == "1":
            pokemonInicial = menu.escolherInicial(pokemons)

            jogador = Jogador(
                equipe = [pokemonInicial],
                localAtual = locais["Ovo"]
            )

            resultado = telaExploracao(jogador, pokemons)
            if resultado == "fim":
                menu.limparTela()
                menu.exibirCentralizado(menu.LOGO)
                print()
                print(f"\033[33m═\033[0m" * largura)
                print()
                printASCII("CONTINUA", delayLetra=0.35, delayLinha=0.008)
                print()
                print()
                print()
                creditos1 = "Jogo desenvolvido por: "
                creditos2 = "Universidade São Judas Tadeu (USJT) ── Ciência da Computação, Unidade Curricular 'Inteligência Artificial'"
                nome1 = "-> \033[31mGustavo Santana Coutinho Silva dos Reis\033[0m"
                nome2 = "-> \033[36mMárcio Almeida Barrocal\033[0m"
                nome3 = "-> \033[92mGabriela Danielly Nascimento\033[0m"
                 
                print(padCenter(creditos1, largura))
                print()
                print(padCenter(nome1, largura))
                print(padCenter(nome2, largura))
                print(padCenter(nome3, largura))
                print()
                print(padCenter(creditos2, largura))
                exit()

        elif escolha == "2":
            menu.limparTela()
            menu.printMENU()
            print(f"\033[33m═\033[0m" * largura)
            print("  ")
            exit()
        else:
            print("  Escolha inválida")

if __name__ == "__main__":
    main()