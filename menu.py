import os
import sys
import re
from itertools import zip_longest
import time

# ── Cores ANSI (mesmo padrão do projeto) ─────────────────────────────────────
RESET = "\033[0m"
V     = "\033[92m"
R     = "\033[31m"
Y     = "\033[33m"
C     = "\033[36m"
O     = "\033[38;5;208m"
BEI   = "\033[38;5;230m"
T     = "\033[38;5;23m"
BRW   = "\033[38;5;58m"
BL    = "\033[34m"
RED   = "\033[31m"
BLA   = "\033[30m"

def limparTela():
    os.system('cls' if os.name == 'nt' else 'clear')
    
def digitar(texto, delay=0.03):
    for ch in texto:
        sys.stdout.write(ch)
        sys.stdout.flush()
        time.sleep(delay)
    print()

def strip_ansi(s):
    return re.sub(r'\033\[[0-9;]*m', '', s)
 
def visible_len(s):
    return len(strip_ansi(s))
 
def pad_to(s, width):
    pad = width - visible_len(s)
    return s + (' ' * pad if pad > 0 else '')
 
def lado_a_lado(lista_esq, lista_dir, espaco=6):
    largura = max(visible_len(l) for l in lista_esq)
    for le, ld in zip_longest(lista_esq, lista_dir, fillvalue=''):
        print(pad_to(le + RESET, largura) + ' ' * espaco + ld)
    
# ── Arte ASCII ────────────────────────────────────────────────────────────────
LOGO = (
    f"\n{Y}"
    f"{'':>16}██████╗  ██████╗ ██╗  ██╗███████╗    ██████╗ ██╗   ██╗████████╗██╗  ██╗ ██████╗ ███╗   ██╗\n"
    f"{'':>16}██╔══██╗██╔═══██╗██║ ██╔╝██╔════╝    ██╔══██╗╚██╗ ██╔╝╚══██╔══╝██║  ██║██╔═══██╗████╗  ██║\n"
    f"{'':>16}██████╔╝██║   ██║█████╔╝ █████╗      ██████╔╝ ╚████╔╝    ██║   ███████║██║   ██║██╔██╗ ██║\n"
    f"{'':>16}██╔═══╝ ██║   ██║██╔═██╗ ██╔══╝      ██╔═══╝   ╚██╔╝     ██║   ██╔══██║██║   ██║██║╚██╗██║\n"
    f"{'':>16}██║     ╚██████╔╝██║  ██╗███████╗    ██║        ██║      ██║   ██║  ██║╚██████╔╝██║ ╚████║\n"
    f"{'':>16}╚═╝      ╚═════╝ ╚═╝  ╚═╝╚══════╝    ╚═╝        ╚═╝      ╚═╝   ╚═╝  ╚═╝ ╚═════╝ ╚═╝  ╚═══╝{RESET}\n"
)

Charizard = [
    O+"⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⣤⣖⠒⠠⠭⠭⠥⠤⠌⢩⣐⡦⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀"+Y+"⠀⠀⠀⣀⠀⠀⠀⠀⠀",
    O+"⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀"+T+"⠈⠁⠈⠉⠒⠢⢄⣕ ⠈⠈⠈"+O+"⠈⠙⠺⢷⣢⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀"+Y+"⠀⣀⣠⢋⡇⠀⣀⠀⠀",
    Y+"⠀⠀⠀⠀⠀⢀⠀⠀"+O+"⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀"+T+"⠈⠒⢄ ⠈⠁"+O+"⠀⠀⠀⠈⠛⢷⣤⣠⡤⠖⡻⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀"+Y+"⠀⠀⠀⢠⣧⠀⠀"+O+"⠙⢲⠂⢽⡀",
    Y+"⠀⠀⢀⡤"+RED+"⢐⡽⠀⠀⠀⠀"+O+"⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀"+T+"⠘⡄ ⠈ ⠈ "+O+"⠀⠀⠀⢻⢀⠖⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣤⡄⠀⠀⠀⠀"+RED+"⠀⠀⠈⢇⢴"+O+"⠘⠫⣅⠀⠀"+Y+"⢰",
    RED+"⡀"+Y+"⢠⠋"+RED+"⡔⠉⠀⠀⠀⠀⠀"+O+"⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀"+T+"⠸⠀⠁ ⠈  ⠈⠈⠈ "+O+"⢸⢸⠀⠀⠀⠀⠀⠀⠀⢀⠤⠤⠄⠒⡫⠋⢀⣀⠀⠀⠀⠀"+RED+"⢀⣠⠤⠼⠐⠋⠲⡀"+Y+"⢠⠃",
    Y+"⠙⢈⢦"+RED+"⠙⣬⢓⢠⠀⠀⠀"+O+"⠀⠀⠀⠀⠀⠀⠀⠀"+T+"⠀⢠⠇  ⠁⠀  ⢄ ⠤⠉"+O+"⢸⢸⠀⠀⠀⠀⠀⢀⠔⠁⠀⠀⢀⣼⣤⣔⣽⣯⣽⠀⠀"+RED+"⠠⣴⢊⠀⡔⠐⢤⡀⠇⠈⠰",
    Y+"⠀⠈⢫⣰"+RED+"⣞⢧⡙⡆⠀⠀"+O+"⠀⠀⠀⠀⠀⠀⠀"+T+"⠀⢀⠎⣠⠆⠁⠁ ⠁  ⠀⡴"+O+"⢸⣾⠀⠀⠀⢀⡴⠉⠀⠀⢀⣰⠟"+BL+"⠦"+O+"⣯⣾⣿⣿⡡"+RED+"⠴⠶⠯⠭⣉⠒⠀"+Y+"⢀⡟⣯⣷⡤⠆",
    Y+"⠀⠀⡔⡗⢏"+RED+"⢨⠈⢿⡄"+O+"⠀⠀⠀⠀⠀⠀⠀⠀"+T+"⢀⣾⣊⣁⣀⠀⠉ ⠁⠈⢀⠜"+O+"⠀⡸⠟⢒⠦⣠⠋⠀⠀⠀⠮⠕⣚⠀⠠⣏⡉⢿⠃⠀⠀⠀⠀"+RED+"⠀"+Y+"⠀⠉⢠⣩⡴⠀⠀⠀⠀",
    Y+"⠀⠀⠣⡇⠀⠀⣀"+RED+"⡾"+O+"⠶⣀⠀⠤⢄⣀⠀⠀⠀⠀⠀⠀⠀⠀"+T+"⠈⠉⠒⢤"+O+"⣖⣲⠶⠋⢥⠲⢧⠀⠙⢄⠀⢀⣠⠤⠒⠉⠀⡷⣽⣿⣦⣷⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀",
    Y+"⠀⠀⠀⠀⠉⠀"+O+"⠀⠀⠉⠒⠨⣕⠂⢄⡙⠶⠤⡀⠀⠀⠀⠀⠀⠀⠀⠈⠉⢹⠛⢿⣢⣃⢨⠀⠀⠀⠟⠉⠀⠀⠀⢀⡼⠒⠚⠻⠿⠿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀",
    O+"⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠢⣌⡑⢤⡀⠑⠢⡀⠀⠀⠀⠀⠀⠀⠁⠀⠈⡠⣶⠟⠀⠀⠀⠀⠀⠀⠀⣴⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀",
    O+"⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⠦⡈⠲⢄⠈⠑⠢⠤⠀⠀⠀⠀⣠⣪⠞⠁⠀"+BEI+"⢀⡠⠤⠠⢄⡀"+O+"⡸⢵⣵⣦⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀",
    O+"⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠢⡈⠑⢄⡀⣀⣀⣠⠖⠋⡝⠁⠀⠀"+BEI+"⡴⠉⠀⠁⠁⠀⢱"+O+"⠃⠀⠙⢟⢧⣦⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀",
    O+"⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠲⢄⡈⠑⢲⠃⠀⡜⠀⠀⠀"+BEI+"⡞⠀⠀⠁⠀⠁⠁⡎"+O+"⠢⡀⠀⠘⡞⣻⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀",
    O+"⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠑⢺⠆⢰⠀⢀⠔"+BEI+"⡿⠀⠁⠁⠀⠁⢀⣰⠙"+O+"⡄⠰⡀⠻⠟⠛⠚⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀",
    O+"⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⠀⠈⡄⢰"+BEI+"⢏⡀⠁⠀⠁⠀⣀⠕⠁"+O+"⠀⡀⡰⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀",
    O+"⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡜⠀⡼⠀⡜⠀⠀"+BEI+"⠉⠉⠁"+O+"⣇⢀⣀⠀⡸⠟⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀",
    O+"⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣈⣣⢤⣧⢤⠇⠀⠀⠀⠀⠀⢸⠿⡈⣾⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀",
    O+"⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀"+RESET+"⠀⠉⢸⡞⠉⡞⠀⠀⠀⠀⠀⠀⠘⡾⣯⣿⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀"+RESET,
]

Pikachu = [
    Y+"⠀⠀⠀⠀⠀⠀⠀⠀⠀⡀⡀⢀⠀⡀⠀⢀⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀",
    Y+"⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⢀⠀⠀⠀⠀⠀⠀⠈⠉⠀⠁⠐⠒⡀⠠⠄⠀⡀⠀⠀⠀⠀",
    Y+"⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠱⡀⠀⠀⢀⠀⠠⠀⠐⠀⠀⠁⠀⠀⠀⡔⠁⠀⠀⠀⠀",
    Y+"⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢌⠈⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⠌⠀⠀⠀⠀⠀⠀",
    Y+"⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠑⠊⠉⠉⠉⠉⠉⠜⠁⠰⠃⠒⠒⢒⣒⠀⠀⠀",
    Y+"⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⠎⣀⠀⠤⠄⡖⣈⠴⠁⠀⠀⠀",
    Y+"⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣾⣿⣯⣄⣀⠀⠀⠀",
    Y+"⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⠀⠊"+BLA+"⣸⣿⡋"+Y+"⣉⣽⠿⠃⠀⠀",
    Y+"⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡠⠴⡿⠣⠀⠂"+BLA+"⣼⣯"+Y+"⡄⠙⠢⡀⠀⠀⠀",
    Y+"⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡠⢂⣥⣶⠃⠀"+BLA+"⢠⣶"+Y+"⠛⢿⣷⡄⠀⠑⡀⠀⠀",
    Y+"⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⠼⠤⠌⠉⠷⠠⡦⠛⠷⣷⣔⠉⠡⠂⡂⠘⡄⠀",
    Y+"⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡠⠂⠀⠁⠀⠀⠀ ⠀⠀⠱⣆⠉⠉⠀⠓⠈⠀⠀⡘⡄",
    Y+"⠀⠀⠀⠀⠀⠀⢀⢀⡀⢀⡰⢀        ⠀⠀⠀⠈⣆⠀⠀⠀⠀⠀⡰⢐⡇",
    Y+"⠀⠀⢀⠤⠒⡈⠁⠂⢀⡠⡅⠀⠀⠀⠀⠀⠀⠀⠀"+BRW+"⢠⣾⣶"+RED+"⣰⣾⡆"+Y+"⠀⠢⢔⣘⡤⢋⠄",
    BLA+"⢠⣶⣿⣷⣷⣤⡤"+Y+"⠍⢒⢋⣅⠀"+BRW+"⢀⣄⣀"+Y+"⠀⠀⠀⠀"+BRW+"⠘⡻⠛"+RED+"⢽⣿⠃"+Y+"⠱⣕⠜⠑⠻⠝⠀",
    Y+"⠀⠀⠀⠀⠀⠀⠀⡰⠥⠄⠸"+RED+"⣄"+BRW+"⣘⢿⡾"+Y+"⠀⢀⠸⣔⣪⠆⣑⡼⠃⠀⠤⠐⣄⠀⠀⠀⠀",
    Y+"⠀⠀⠀⠀⠀⠀⢠⡁⢆⣜⠔"+RED+"⠊⠛"+Y+"⢷⣄⣤⣉⢍⡰⠔⠊⠉⠈⠒⠛⠦⠵⠞⠀⠀⠀⠀",
    Y+"⠀⠀⠀⠀⠀⠀⠀⠉⠉⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀"+RESET,
    ]

def printMENU():
    print(LOGO)
    lado_a_lado(Charizard, Pikachu)

LARGURA = 124

def exibirMenu():
    limparTela()
    printMENU()
    print()
    print(f"\033[33m═\033[0m" * LARGURA)
    print(f"\033[33m{'★  MENU PRINCIPAL  ★':^{LARGURA}}\033[0m")
    print(f"\033[33m═\033[0m" * LARGURA)
    print()
    print(f"  [\033[33m1\033[0m] \033[92mIniciar Jogo\033[0m")
    print(f"  [\033[33m2\033[0m] \033[31mFechar\033[0m")
    print()
    print("─" * LARGURA)

def escolherInicial(pokemons):
    limparTela()
    print(LOGO)
    print()

    digitar(f"  {Y}Você sente uma sensação antiga...{RESET}", delay=0.04)
    time.sleep(0.6)
    digitar(f"  {Y}Algo está te chamando, de muito longe...{RESET}", delay=0.04)
    time.sleep(0.8)
    digitar(f"  {Y}Porém, você...{RESET}", delay=0.05)
    time.sleep(1.2)
    digitar(f"  {Y}Quem é você?{RESET}", delay=0.07)
    time.sleep(1.0)

    print()
    print(f"\033[33m─\033[0m" * LARGURA)
    print()

    opcoes = [
        (f"  [{Y}1{RESET}]", f"{R}Minha vontade queima como fogo, e disso eu sou feito.{RESET}", "Chimchar",  f"{R}Chimchar{RESET}"),
        (f"  [{Y}2{RESET}]", f"{C}Minha vontade flui como água, e disso eu sou feito.{RESET}", "Totodile",    f"{C}Totodile{RESET}"),
        (f"  [{Y}3{RESET}]", f"{V}Minha vontade cresce como as plantas, e disso eu sou feito.{RESET}", "Rowlet", f"{V}Rowlet{RESET}"),
    ]

    for prefixo, frase, _, _ in opcoes:
        time.sleep(0.3)
        digitar(f"{prefixo} {frase}", delay=0.025)

    print()
    print(f"\033[33m─\033[0m" * LARGURA)

    while True:
        escolha = input(f"\n  {Y}>{RESET} ").strip()

        if escolha in ("1", "2", "3"):
            _, frase, nome, nomeColorido = opcoes[int(escolha) - 1]
            print()
            time.sleep(0.5)
            digitar(f"  {Y}...{RESET}", delay=0.1)
            time.sleep(0.8)
            digitar(f"  {Y}Você é um {nomeColorido}{Y}!{RESET}", delay=0.06)
            time.sleep(1.0)
            print()
            input(f"  {Y}Pressione Enter para começar sua jornada...{RESET}")
            return pokemons[nome]
        print(f"  Escolha inválida.")
